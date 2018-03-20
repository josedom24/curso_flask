# Gestión de usuarios con extensión Flask-Login

En las unidades anteriores hemos gestionado las sesiones con Flask de manera manual, gestionando las variables de sesión (fichero `login.py`) directamente y comprobando su existencia para el control de acceso.

En esta unidad vamos a introducir una nueva extensión de Flask que nos permite trabajar con sesiones: [Flask-Login](https://flask-login.readthedocs.io/en/latest/).

ˋFlask-Loginˋ es una librería que nos proporciona la posibilidad de gestionar las sesiones de nuestros usuarios; se ocupa de las tareas comunes: como el inicio de sesión, logout y recordar las sesiones de los usuarios durante periodos de tiempo personalizados.

Con esta extensión podemos almacenar el identificador de la sesión del usuario activo, y nos permite abrir o cerrar una sesión, nos permite restringir vistas o rutas a usuarios sin sesión activa. Con esta extensión no podemos restringir el comportamiento de una vista según el rol de usuario.

## Instalación y configuración de flask-login

Con nuestro entorno virtual activado:

	pip install Flask-Login

En el programa principal configuramos la extensión:

	from flask_login import LoginManager,login_user,logout_user,login_required,current_user
	...

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = "login"

Flask-Login nos provee de diversas funciones muy interesantes para el uso de sesiones y a continuación te presento las más interesantes:

* `login_user`: Esta función permite crear la sesión de un usuario.
* `logout_user`: Esta función permite terminar la sesión actual.
* `login_required`: Es un decorador que nos permite restringir la ejecución de una vista sólo a los usuarios logueados.
* `current_user`: Es un objeto con la información del usuario autentificado.

## Revisando el modelo de datos

En el modelo de datos que representa los usuarios hay que añadirle los siguiente nuevos métodos:

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def is_admin(self):
		return self.admin


* `is_authenticated`: Devuelve "True" si el usuario se autentifica, es decir, que ha proporcionado unas credenciales válidas.
* `is_active`: Devuelve "True" si el usuario se encuentra activo. Además de ser autenticado, también han activado su cuenta, no se ha suspendido, o cualquier condición que su aplicación requiera para rechazar una cuenta. Esto no lo hemos tenido en cuenta en nuestro modelo de datos.
* `is_anonymous`: Retorna "True" si se detecta que es la sesión de usuario anónimo. La respuesta es "False" cuando se detecta que es un usuario con unas sesión correcta.
* `get_id`: Nos devuelve una cadena en Unicode que identifica de forma única a un usuario logueado en el sistema.
* `is_admin`: devuelve "True" si el usuario logueado es administrador.

{% include "../../adsense.md" %}

## Llamando al cargador de User

La extensión Flask-Login no nos permite acceder directamente a la tabla de usuarios para obtener la información de un determinado usuario, por lo tanto en el programa principal tenemos que escribir una función que va a utilizar Flask-Login:

	@login_manager.user_loader
	def load_user(user_id):
		return Usuarios.query.get(int(user_id))

## Control de acceso

Por ejemplo, para poder cambiar la contraseña el usuario tiene que estar logueado, para restringir el acceso utilizamos el decorador `login_required`:

	@app.route('/changepassword/<username>', methods=["get","post"])
	@login_required
	def ...

Sin embrgo si queremos restringuir por el rol, por ejemplo: la ruta `/articulos/new` que nos permite añadir un videojuego sólo se debería permitir a los usuarios adminitradores, deberáimos codificarlo de la siguiente manera:

	@app.route('/articulos/new', methods=["get","post"])
	@login_required
	def articulos_new():
		if not current_user.is_admin():
			abort(404)


Otro ejemplo, sólo podemos registrarnos si no estamos con un usuario logueado, por lo tento en la ruta `registro` preguntamos:

	@app.route("/registro",methods=["get","post"])
	def registro():
		if current_user.is_authenticated:
			return redirect(url_for("inicio"))

## Generando contenido según el tipo de usuario

Además del control de acceso anterior tenemos que hacer que las plantillas generen contenido distintos según el tipo de usuario que tengamos en el sistema.

Por ejemplo, sólo le debemos mostrar el enlace de añadir videojuegos a los usuarios administradores, para ello en la plantilla `inicio.html`:

	{% raw %}
	{% if current_user.is_authentificated and current_user.is_admin() %}
    	<a class="btn btn-primary" href="{{url_for('articulos_new')}}" role="button">Nuevo videojuego</a>
 	{% endif %}
 	{% endraw %}

Otro ejemplo, mostramos la opción de "Registro" y "Login" para los usuarios invitados, y la opción de "Perfil" y de "Salir" para los usuarios logueados, para ello en la plantilla `base.html`:

	{% if current_user.is_authenticated %}
        <a class="navbar-brand " href="/perfil/{{ session["username"]}}"> Perfil</a>
        <a class="navbar-brand " href="/logout"> {{ session["username"]}} (Salir)</a>
    {% else %}
        <a class="navbar-brand " href="/login">Login</a>
        <a class="navbar-brand " href="/registro">Registro</a>
    {% endif %} 

Para terminar con otro ejemplo, solo los administradores pueden modificar y borrar videojuegos, y los usuarios logueados pueden comprar, en la plantilla `inicio.html` tenemos el siguiente código:

	{% if current_user.is_authentificated and current_user.is_admin() %}
        <td><a href="{{url_for('articulos_edit',id=art.id)}}"><span class="glyphicon glyphicon-pencil"></span> Modificar</a></td>
        <td><a href="{{url_for('articulos_delete',id=art.id)}}"><span class="glyphicon glyphicon-trash"></span> Borrar</a></td>
    {% endif %}   

    {% if current_user.is_authenticated %}
        <td><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span> Comprar</a></td>
    {% endif %}   

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u30)

{% include "../../adsense2.md" %}