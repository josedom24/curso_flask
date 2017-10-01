# Gestión de permisos de usuarios

En esta unidad vamos a estudiar como autorizar las distintas acciones que pueden hacer nuestros usuarios en la aplicación. Cuando accedemos a la aplicación podemos hacerlo de tres formas distintas:

* Usuario invitado: Navegamos por la página sin autentificar ningún usuario del sistema.
* Usuario normal: Nos hemos autentificado con un usuario que no es administrador.
* Usuario administrador: Nos hemos autentificado con un usuario administrador.

## Control de acceso

Veamos una tabla donde indicamos según el tipo de usuario con el que estamos trabajando las distintas acciones que se pueden realizar:

| Acción   | Invitado | Normal | Administrador |
| :------- | :------: | :----: | :-----------: |
| Hacer login | Si | No | No |
| Registrarse | Si | No | No |
| Ver perfil | No | Si | Si |
| Puede cambiar la contraseña | No | Si | Si |
| Puede ver los videojuegos | Si | Si | Si |
| Puede ver las categorías | Si | Si | Si |
| Puede añadir categorías y videojuegos | No | No | Si |
| Puede modificar y borrar categorías y videojuegos | No | No | Si |
| Puede comprar videojuegos | No | Si | Si |

## ¿Cómo determinamos la clase de usuario con el que estamos trabajando?

En la unidad anterior, preguntábamos por la existencia de las variables de sesión:

* Que estás logueado (usuario normal):

		if session["id"]

* Qué estás logueado y es administrador:

		if session["admin"]

En esta unidad vamos a crear dos funciones en el fichero `login.py` para realizar esta tarea de forma más elegante:

	def is_login():
		if "id" in session:
			return True
		else:
			return False	

	def is_admin():
		return session.get("admin",False) 

Por otro lado, en unidades anteriores no teníamos ningún problema al preguntar por la variable `session` en las plantillas, si queremos hacerlo un poco más elegante podríamos crear dos variables en el contexto de las plantillas que me permitan determinar el rol del usuario, para ello en el mismo fichero `login.py`:

	@app.context_processor
	def login():
		if "id" in session:
			return {'is_login':True}
		else:
			return {'is_login':False}	

	@app.context_processor
	def admin():
		return {'is_admin':session.get("admin",False) }

Donde creamos dos variables: `is_login` y `is_admin` que podemos utilizar en las plantillas.

## Control de acceso

Por ejemplo la ruta `/articulos/new` que nos permite añadir un videojuego sólo se debería permitir a los usuarios administradores, por lo que al principio realizamos la comprobación:

	if not is_admin():
		abort(404)

Otro ejemplo, sólo podemos registrarnos si no estamos con un usuario logueado, por lo tanto en la ruta `registro` preguntamos:

	if is_login():
		return redirect(url_for("inicio"))

## Generando contenido según el tipo de usuario

Además del control de acceso anterior tenemos que hacer que las plantillas generen contenido distintos según le tipo de usuario que tengamos en el sistema.

Por ejemplo, sólo le debemos mostrar el enlace de añadir videojuegos a los usuarios administradores, para ello en la plantilla `inicio.html`:

	{% if is_admin %}
    	<a class="btn btn-primary" href="{{url_for('articulos_new')}}" role="button">Nuevo videojuego</a>
    {% endif %}

Otro ejemplo, mostramos la opción de "Registro" y "Login" para los usuarios invitados, y la opción de "Perfil" y de "Salir" para los usuarios logueados, para ello en la plantilla `base.html`:

	{% if is_login %}
        <a class="navbar-brand " href="/perfil/{{ session["username"]}}"> Perfil</a>
        <a class="navbar-brand " href="/logout"> {{ session["username"]}} (Salir)</a>
    {% else %}
        <a class="navbar-brand " href="/login">Login</a>
        <a class="navbar-brand " href="/registro">Registro</a>
    {% endif %} 

Para terminar con otro ejemplo, solo los administradores pueden modificar y borrar videojuegos, y los usuarios logueados pueden comprar, en la plantilla `inicio.html` tenemos el siguiente código:

	{% if is_admin %}
        <td><a href="{{url_for('articulos_edit',id=art.id)}}"><span class="glyphicon glyphicon-pencil"></span> Modificar</a></td>
        <td><a href="{{url_for('articulos_delete',id=art.id)}}"><span class="glyphicon glyphicon-trash"></span> Borrar</a></td>
    {% endif %}   

    {% if is_login %}
        <td><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span> Comprar</a></td>
    {% endif %}   

## Código ejemplo de esta unidad

[Código](../../ejemplos/u29)