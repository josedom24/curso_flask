from flask import Flask, render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import formCategoria

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

from aplicacion.models import Articulos,Categorias
@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
	categoria=Categorias.query.get(id)
	if id=='0':
		articulos=Articulos.query.all()
	else:
		articulos=Articulos.query.filter_by(CategoriaId=id)
	categorias=Categorias.query.all()
	return render_template("inicio.html",articulos=articulos,categorias=categorias,categoria=categoria)

@app.route('/categorias')
def categorias():
	categorias=Categorias.query.all()
	return render_template("categorias.html",categorias=categorias)

@app.route('/categorias/new', methods=["get","post"])
def categorias_new():
	form=formCategoria(request.form)
	if form.validate_on_submit():
		cat=Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect(url_for("categorias"))
	else:
		return render_template("categorias_new.html",form=form)
	


@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

