from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Tabla(db.Model):
    __tablename__ = "Blog"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    titulo = db.Column(db.String)
    texto = db.Column(db.String)


def posts(usuario):
    quer = db.session.query(Tabla).filter(Tabla.username == usuario).order_by(Tabla.texto.desc()).limit(3)
    query = quer.all()
    posts_dict_1 = {}
    posts_dict_2 = {}
    posts_dict_3 = {}
    posts_list = []

    for dato in query:
        if len(posts_dict_1) == 0:
            posts_dict_1["titulo"] = dato.titulo
            posts_dict_1["texto"] = dato.texto
            posts_list.append(posts_dict_1)
        elif len(posts_dict_2) == 0:
            posts_dict_2["titulo"] = dato.titulo
            posts_dict_2["texto"] = dato.texto
            posts_list.append(posts_dict_2)
        elif len(posts_dict_3) == 0:
            posts_dict_3["titulo"] = dato.titulo
            posts_dict_3["texto"] = dato.texto
            posts_list.append(posts_dict_3)

    return posts_list


def insert(title,text,usuario):
    nuevo = Tabla(titulo = title, texto = text, username = usuario)

    db.session.add(nuevo)
    db.session.commit()

    return nuevo

def Eliminar(usuario):
    query = db.session.query(Tabla).filter(Tabla.username == usuario).all()

    for line in query:
        db.session.delete(line)
        db.session.commit()

    return 

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdatabase.db"
    # Bindear la DB con nuestra app Flask
    db.init_app(app)
    app.app_context().push()

    db.create_all()

    # Aquí se puede ensayar todo lo que necesitemos con nuestra DB
    # ...

    db.session.remove()
    db.drop_all()