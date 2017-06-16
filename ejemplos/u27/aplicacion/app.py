from flask import Flask, render_template,redirect,url_for,request,abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import formCategoria,formArticulo,formSINO,LoginForm
from werkzeug.utils import secure_filename
from flask_login import LoginManager,login_user,logout_user,login_required,current_user

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from aplicacion.models import Articulos,Categorias,Usuarios
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
@login_required
def categorias():
	if not current_user.is_admin():
		abort(404)
	categorias=Categorias.query.all()
	return render_template("categorias.html",categorias=categorias)

@app.route('/categorias/new', methods=["get","post"])
@login_required
def categorias_new():
	if not current_user.is_admin():
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
@login_required
def categorias_edit(id):
	if not current_user.is_admin():
		abort(404)
	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)

	form=formCategoria(request.form,obj=cat)
		
	if form.validate_on_submit():
		form.populate_obj(cat)
		db.session.commit()
		return redirect(url_for("categorias"))

	
	return render_template("categorias_new.html",form=form)

@app.route('/categorias/<id>/delete', methods=["get","post"])
def categorias_delete(id):
	cat=Categorias.query.get(id)
	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(cat)
			db.session.commit()
		return redirect(url_for("categorias"))
	return render_template("categorias_delete.html",form=form,cat=cat)

@app.route('/articulos/new', methods=["get","post"])
def articulos_new():
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
	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formArticulo(request.form,obj=art)
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	
	if form.validate_on_submit():
		form.populate_obj(art)
		db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/delete', methods=["get","post"])
def articulos_delete(id):
	art=Articulos.query.get(id)
	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(art)
			db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_delete.html",form=form,art=art)

@login_manager.user_loader
def load_user(user_id):
	return Usuarios.query.get(int(user_id))

@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	user=Usuarios.query.filter_by(username=form.username.data).first()
    	if user!=None and user.is_active and user.verify_password(form.password.data):
    		login_user(user)
    		next = request.args.get('next')
    		#if not is_safe_url(next):
    			#return abort(400)
    		return redirect(next or url_for('inicio'))
    	
    	form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('login.html', form=form)
@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

