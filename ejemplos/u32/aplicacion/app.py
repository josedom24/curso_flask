from flask import Flask, render_template, redirect, url_for, request, abort, \
    session, make_response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import FormCategoria, FormArticulo, FormSINO, LoginForm,\
    FormUsuario, FormChangePassword, FormCarrito
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
import os
import json

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
    from aplicacion.models import Articulos, Categorias
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
    from aplicacion.models import Categorias
    categorias = Categorias.query.all()
    return render_template("categorias.html", categorias=categorias)


@app.route('/categorias/new', methods=["get", "post"])
@login_required
def categorias_new():
    from aplicacion.models import Categorias
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormCategoria(request.form)
    if form.validate_on_submit():
        cat = Categorias(nombre=form.nombre.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("categorias"))
    else:
        return render_template("categorias_new.html", form=form)


@app.route('/categorias/<id>/edit', methods=["get", "post"])
@login_required
def categorias_edit(id):
    from aplicacion.models import Categorias
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Categorias.query.get(id)
    if cat is None:
        abort(404)
    form = FormCategoria(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("categorias"))
    return render_template("categorias_new.html", form=form)


@app.route('/categorias/<id>/delete', methods=["get", "post"])
@login_required
def categorias_delete(id):
    from aplicacion.models import Categorias
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Categorias.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("categorias"))
    return render_template("categorias_delete.html", form=form, cat=cat)


@app.route('/articulos/new', methods=["get", "post"])
@login_required
def articulos_new():
    from aplicacion.models import Articulos, Categorias
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormArticulo()
    categorias = [(c.id, c.nombre) for c in Categorias.query.all()[1:]]
    form.CategoriaId.choices = categorias
    if form.validate_on_submit():
        try:
            f = form.photo.data
            nombre_fichero = secure_filename(f.filename)
            f.save(app.root_path + "/static/upload/" + nombre_fichero)
        except:
            nombre_fichero = ""
        art = Articulos()
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("inicio"))
    else:
        return render_template("articulos_new.html", form=form)


@app.route('/articulos/<id>/edit', methods=["get", "post"])
@login_required
def articulos_edit(id):
    from aplicacion.models import Articulos, Categorias
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    art = Articulos.query.get(id)
    if art is None:
        abort(404)
    form = FormArticulo(obj=art)
    categorias = [(c.id, c.nombre) for c in Categorias.query.all()[1:]]
    form.CategoriaId.choices = categorias
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+"/static/upload/"+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + "/static/upload/" + nombre_fichero)
            except:
                nombre_fichero = ""
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("articulos_new.html", form=form)


@app.route('/articulos/<id>/delete', methods=["get", "post"])
@login_required
def articulos_delete(id):
    from aplicacion.models import Articulos
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    art = Articulos.query.get(id)
    if art is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            if art.image != "":
                os.remove(app.root_path+"/static/upload/"+art.image)
            db.session.delete(art)
            db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("articulos_delete.html", form=form, art=art)


@app.route('/login', methods=['get', 'post'])
def login():
    from aplicacion.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('inicio'))
        form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/registro", methods=["get", "post"])
def registro():
    from aplicacion.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))
    form = FormUsuario()
    if form.validate_on_submit():
        existe_usuario = Usuarios.query.\
            filter_by(username=form.username.data).first()
        if existe_usuario is None:
            user = Usuarios()
            form.populate_obj(user)
            user.admin = False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("inicio"))
        form.username.errors.append("Nombre de usuario ya existe.")
    return render_template("usuarios_new.html", form=form)


@app.route('/perfil/<username>', methods=["get", "post"])
@login_required
def perfil(username):
    from aplicacion.models import Usuarios
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    form = FormUsuario(request.form, obj=user)
    del form.password
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("usuarios_new.html", form=form, perfil=True)


@app.route('/changepassword/<username>', methods=["get", "post"])
@login_required
def changepassword(username):
    from aplicacion.models import Usuarios
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    form = FormChangePassword()
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("changepassword.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models import Usuarios
    return Usuarios.query.get(int(user_id))


@app.route('/carrito/add/<id>', methods=["get", "post"])
@login_required
def carrito_add(id):
    from aplicacion.models import Articulos
    art = Articulos.query.get(id)
    form = FormCarrito()
    form.id.data = id
    if form.validate_on_submit():
        if art.stock >= int(form.cantidad.data):
            try:
                datos = json.loads(request.cookies.get(str(current_user.id)))
            except:
                datos = []
            actualizar = False
            for dato in datos:
                if dato["id"] == id:
                    dato["cantidad"] = form.cantidad.data
                    actualizar = True
            if not actualizar:
                datos.append({"id": form.id.data,
                              "cantidad": form.cantidad.data})
            resp = make_response(redirect(url_for('inicio')))
            resp.set_cookie(str(current_user.id), json.dumps(datos))
            return resp
        form.cantidad.errors.append("No hay artículos suficientes.")
    return render_template("carrito_add.html", form=form, art=art)


@app.route('/carrito')
@login_required
def carrito():
    from aplicacion.models import Articulos
    try:
        datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    articulos = []
    cantidades = []
    total = 0
    for articulo in datos:
        articulos.append(Articulos.query.get(articulo["id"]))
        cantidades.append(articulo["cantidad"])
        total = total + Articulos.query.get(articulo["id"]).precio_final() * \
            articulo["cantidad"]
    articulos = zip(articulos, cantidades)
    return render_template("carrito.html", articulos=articulos, total=total)


@app.route('/carrito_delete/<id>')
@login_required
def carrito_delete(id):
    try:
        datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    new_datos = []
    for dato in datos:
        if dato["id"] != id:
            new_datos.append(dato)
    resp = make_response(redirect(url_for('carrito')))
    resp.set_cookie(str(current_user.id), json.dumps(new_datos))
    return resp


@app.context_processor
def contar_carrito():
    if not current_user.is_authenticated:
        return {'num_articulos': 0}
    if request.cookies.get(str(current_user.id)) is None:
        return {'num_articulos': 0}
    else:
        datos = json.loads(request.cookies.get(str(current_user.id)))
        return {'num_articulos': len(datos)}


@app.route('/pedido')
@login_required
def pedido():
    from aplicacion.models import Articulos
    try:
        datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    total = 0
    for articulo in datos:
        total = total + Articulos.query.get(articulo["id"]).precio_final() * \
            articulo["cantidad"]
        Articulos.query.get(articulo["id"]).stock -= articulo["cantidad"]
        db.session.commit()
    resp = make_response(render_template("pedido.html", total=total))
    resp.set_cookie(str(current_user.id), "", expires=0)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404
