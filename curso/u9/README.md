# Enrutamiento: rutas

El objeto Flask `app` nos proporciona un decorador `router` que es capaz de filtrar la función *vista* que se va ejecutar analizando la petición HTTP, fundamentalmente por la ruta y el método que se hace la petición.

## Trabajando con rutas

Veamos un ejemplo:

	...
	@app.route('/')
	def inicio():
	    return 'Página principal'	

	@app.route('/articulos/')
	def articulos():
	    return 'Lista de artículos'	

	@app.route('/acercade')
	def acercade():
	    return 'Página acerca de...'

En este caso se comprueba la ruta de la petición HTTP, y cuando coincide con alguna indicada en las rutas se ejecuta la función correspondiente devolviendo una respuesta HTTP. 

	curl http://localhost:5000
	Página principal

Si declaramos rutas terminando en `/` son consideradas como un directorio de un sistema de fichero, en este caso si se accede a la ruta sin la barra final se producirá una redirección a la ruta correcta.

	curl http://localhost:5000/articulos/
	Lista de artículos

	curl http://localhost:5000/articulos
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
	<title>Redirecting...</title>
	<h1>Redirecting...</h1>
	<p>You should be redirected automatically to target URL: <a href="http://localhost:5000/articulos/">http://localhost:5000/articulos/</a>.  If not click the link.

Si declaramos la rutas sin `/` final, se consideran un fichero del sistema de fichero, si accedemos a la ruta con el `/` nos devolverá una respuesta con código 404.

	curl http://localhost:5000/acercade
	Página acerca de...

	curl http://localhost:5000/acercade/ 
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
	<title>404 Not Found</title>
	<h1>Not Found</h1>
	<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

Si la ruta de la petición HTTP no corresponde con ninguna que hayamos indicado se devolverá una respuesta con código de estado 404 indicando que no se ha encontrado el recurso.

{% include "../../adsense3.md" %}

## Rutas dinámicas

Podemos gestionar rutas variables, es decir que correspondan a un determinado patrón o expresión regular, por ejemplo:

	@app.route("/articulos/<int:id>")
	def mostrar_ariculo(id):
		return 'Vamos a mostrar el artículo con id:{}'.format(id)

	curl http://localhost:5000/articulos/6                                      
	Vamos a mostrar el artículo con id:6

Otro ejemplo:

	@app.route("/hello/")
	@app.route("/hello/<string:nombre>")
	@app.route("/hello/<string:nombre>/<int:edad>")
	def hola(nombre=None,edad=None):
		if nombre and edad:
			return 'Hola, {0} tienes {1} años.'.format(nombre,edad)
		elif nombre:
			return 'Hola, {0}'.format(nombre)
		else:
			return 'Hola mundo'

	curl http://localhost:5000/hello/
	Hola mundo

	curl http://localhost:5000/hello/pepe
	Hola, pepe

	curl http://localhost:5000/hello/pepe/16
	Hola, pepe tienes 16 años.

La parte dinámica de la ruta la podemos obtener como variable que recibe la función correspondiente. En el segundo ejemplo, además observamos que varias rutas pueden ejecutar una misma función. Aunque no es obligatorio podemos especificar el tipo de la variable capturada:

* `string`: Acepta cualquier texto sin barras (por defecto)
* `int`: Acepta enteros
* `float`: Acepta valores reales
* `path`: Acepta cadena de caracteres con barras

## Construcción de rutas

Podemos importar la función `url_for` que nos permite construir rutas a partir del nombre de la función asociada:

	python3 manage shell

	In [1]: from flask import url_for

	In [2]: url_for('articulos')
	Out[2]: '/articulos/'

	In [3]: url_for('hola',nombre="pepe")
	Out[3]: '/hello/pepe'

	In [4]: url_for('hola',nombre="pepe",edad=40)
	Out[4]: '/hello/pepe/40'

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u9)

{% include "../../adsense2.md" %}