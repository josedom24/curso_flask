# Gestión de permisos de usuarios

En esta unidad vamos a estudiar como autorizar las distintas acciones que pueden hacer nuestro usuarios en la aplicación. Cuando accedemos a la aplicación podemos hacerlo de tres formas distintas:

* Usuario invitado: Navegamos por la página sin autentificar ningún usuario del sistema.
* Usuario normal: Nos hemos autentificado con un usuario que no es administrador.
* Usuario administrador: Nos hemos autentificado con un usuario administrador.

## Control de acceso

Veamos una tabla donde indicamos según el tipo de usuario con el que estamos trabajnfo las distintas acciones que se pueden realizar:

| Acción   | Invitado | Normal | Administrador |
| :------- | :------: | :----: | :-----------: |
| Hacer login | Si | No | No |
| Registrarse | Si | No | No |
| Ver perfil | No | Si | Si |
| Puede cambiar la contraseña | No | Si | Si |
| Puede ver los videojuegos | Si | Si | Si |
| Puede ver las categorías | Si | Si | Si |
| Puede añadir categorias y videojuegos | No | No | Si |
| Puede modificar y borrar categorias y videojuegos | No | No | Si |
| Puede comprar videojuegos | No | Si | Si |

## ¿Cómo determinado la clase de usuario con el que estamos trabajando?

En la unidad anterior, preguntabmos por la existencia de las variables de sesión:

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

Oir itri lado, en unidades anteriores no teníamos ningún problema al preguntar por la variable `session` en las plantillas, si queremos hacerlo un poco más elegante podríamos crear dos variables en el contexto de las plantillas que me permitan determinar el rol del usuario, para ello en el mismo fichero `login.py`:

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

Por ejemplo la ruta `/articulos/new` que nos permite añadir un videojuego sólo se debería permitir a los usuarios adminitradores, por lo que al principio realizamos la comprobación:

	if not is_admin():
		abort(404)

Otro ejemplo, sólo podemos registrarnos si no estamos con un usuario logueado, por lo tento en la ruta `registro` preguntamos:

	if is_login():
		return redirect(url_for("inicio"))