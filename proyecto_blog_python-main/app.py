import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for

import blog

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///blog.db"
blog.db.init_app(app)


@app.route("/")
def index():
    try:
        return render_template("blog.html")
    except:
        return jsonify({"trace": traceback.format_exc})


@app.route("/login")
def login():
    try:
        return render_template("login.html")
    except:
        return jsonify({"trace": traceback.format_exc})


@app.route("/posteos/<usuario>", methods=["GET", "POST"])
def usuario_GET_POST(usuario):
    if request.method == "GET":
        posts = blog.posts(usuario)
        return jsonify({"posts": posts})
    if request.method == "POST":
        titulo = str(request.form.get("titulo"))
        texto = str(request.form.get("texto"))
        post = blog.insert(titulo, texto, usuario)

        return jsonify({"id": post.id, "titulo": post.titulo, "texto": post.texto})


@app.route("/borrar/<usuario>", methods =[ "GET", "POST"])
def borrar(usuario):
    blog.delete(usuario)
    print("hola")
    return redirect("/")


@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos
    blog.db.create_all()
    print("Base de datos generada")


if __name__ == "__main__":
    app.run(host="http://localhost:8080", port=5000)
