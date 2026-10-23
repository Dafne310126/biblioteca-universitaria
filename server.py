
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        titulo="Inicio",
        mensaje="Bienvenido a nuestra biblioteca universitaria"
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Descubre los materiales disponibles para tu aprendizaje"
    )


@app.route("/servicios")
def servicios():
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios que tenemos para ti"
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Estamos para ayudarte con tus consultas"
    )


if __name__ == "__main__":
    app.run(debug=True)
