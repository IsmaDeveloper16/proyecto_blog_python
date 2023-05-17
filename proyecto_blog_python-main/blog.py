from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    titulo = db.Column(db.String)
    texto = db.Column(db.String)


def posts(usuario):
    quer = db.session.query(blog).filter(blog.username == usuario).order_by(blog.texto.desc()).limit(3)
    query = quer.all()
    posts_dict_1 = {}
    posts_list = []

    for dato in query:
        if len(posts_dict_1) == 0:
            posts_dict_1["text_1"] = dato.texto
        elif len(posts_dict_1) == 1:
            posts_dict_1["text_2"] = dato.texto
        elif len(posts_dict_1) == 2:
            posts_dict_1["text_3"] = dato.texto

    posts_list.append(posts_dict_1)
    return posts_list


def insert(title,text,usuario):
    nuevo = blog(titulo = title, texto = text, username = usuario)

    db.session.add(nuevo)
    db.session.commit()

    return nuevo

def delete(usuario):
    db.session.delete(blog).filter(blog.username == usuario)
    db.session.commit()


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