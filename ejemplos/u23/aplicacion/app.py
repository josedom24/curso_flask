from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)

from aplicacion.models import Articulos, Categorias


@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
    categoria = Categorias.query.get(id)
    if id == '0':
        articulos = Articulos.query.all()
    else:
        articulos = Articulos.query.filter_by(CategoriaId=id)
    categorias = Categorias.query.all()
    return render_template("inicio.html", articulos=articulos,
                           categorias=categorias, categoria=categoria)


@app.route('/categorias')
def categorias():
    categorias = Categorias.query.all()
    return render_template("categorias.html", categorias=categorias)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404
