from flask import Flask, render_template,redirect,url_for,request,abort,session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import formCategoria,formArticulo,formSINO,LoginForm,formUsuario,formChangePassword
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

from aplicacion.models import Articulos,Categorias,Usuarios
from aplicacion.login import login_user,logout_user,is_login,is_admin

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
	# Control de permisos
	if not is_admin():
		abort(404)

	form=formCategoria(request.form)
	if form.validate_on_submit():
		cat=Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect(url_for("categorias"))
	else:
		return render_template("categorias_new.html",form=form)

@app.route('/categorias/<id>/edit', methods=["get","post"])
def categorias_edit(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)

	form=formCategoria(request.form,obj=cat)
		
	if form.validate_on_submit():
		form.populate_obj(cat)
		db.session.commit()
		return redirect(url_for("categorias"))

@app.route('/categorias/<id>/delete', methods=["get","post"])
def categorias_delete(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)
	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(cat)
			db.session.commit()
		return redirect(url_for("categorias"))
	return render_template("categorias_delete.html",form=form,cat=cat)

@app.route('/articulos/new', methods=["get","post"])
def articulos_new():
	# Control de permisos
	if not is_admin():
		abort(404)

	form=formArticulo()
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	if form.validate_on_submit():
		try:
			f = form.photo.data
			nombre_fichero=secure_filename(f.filename)
			f.save(app.root_path+"/static/upload/"+nombre_fichero)
		except:
			nombre_fichero=""
		art=Articulos()
		form.populate_obj(art)
		art.image=nombre_fichero
		db.session.add(art)
		db.session.commit()
		return redirect(url_for("inicio"))
	else:
		return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/edit', methods=["get","post"])
def articulos_edit(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formArticulo(obj=art)
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	
	if form.validate_on_submit():
		#Borramos la imagen anterior
		if art.image!="":
			os.remove(app.root_path+"/static/upload/"+art.image)
		try:
			f = form.photo.data
			nombre_fichero=secure_filename(f.filename)
			f.save(app.root_path+"/static/upload/"+nombre_fichero)
		except:
			nombre_fichero=""
		form.populate_obj(art)
		
		art.image=nombre_fichero
		db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/delete', methods=["get","post"])
def articulos_delete(id):
		# Control de permisos
	if not is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			os.remove(app.root_path+"/static/upload/"+art.image)
			db.session.delete(art)
			db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_delete.html",form=form,art=art)


@app.route('/login', methods=['get', 'post'])
def login():
	# Control de permisos
	if is_login():
		return redirect(url_for("inicio"))

	form = LoginForm()
	if form.validate_on_submit():
		user=Usuarios.query.filter_by(username=form.username.data).first()
		if user!=None and user.verify_password(form.password.data):
			login_user(user)
			return redirect(url_for('inicio'))
		form.username.errors.append("Usuario o contraseña incorrectas.")
	return render_template('login.html', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/registro",methods=["get","post"])
def registro():
	# Control de permisos
	if is_login():
		return redirect(url_for("inicio"))

	form=formUsuario()
	if form.validate_on_submit():
		existe_usuario=Usuarios.query.filter_by(username=form.username.data).first()
		if existe_usuario==None:
			user=Usuarios()
			form.populate_obj(user)
			user.admin=False
			db.session.add(user)
			db.session.commit()
			return redirect(url_for("inicio"))
		form.username.errors.append("Nombre de usuario ya existe.")
	return render_template("usuarios_new.html",form=form)

@app.route('/perfil/<username>', methods=["get","post"])
def perfil(username):
	# Control de permisos
	if not is_login():
		abort(404)
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formUsuario(request.form,obj=user)
	del form.password	
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("usuarios_new.html",form=form,perfil=True)

@app.route('/changepassword/<username>', methods=["get","post"])
def changepassword(username):
	# Control de permisos
	if not is_login():
		abort(404)
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formChangePassword()
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("changepassword.html",form=form)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

