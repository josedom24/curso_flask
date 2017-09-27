# Píldora 2: Mi primer programa en flask
## Instalación de flask

Vamos a realizar la instalación de Flask utilizando la herramienta `pip` en un entorno virtual creado con `virtualenv`. La instalación de Flask depende de dos paquetes: [Werkzeug](http://werkzeug.pocoo.org/), una librería WSGI para Python y [jinja2](http://jinja.pocoo.org/docs/2.9/) como motor de plantillas.

## Creando el entorno virtual

Como Flask es compatible con python3 vamos a crear un entorno virtual compatible con la versión 3 del interprete python. Para ello nos aseguremos que tenemos la utilidad instalada:

	# apt-get install python-virtualenv

Y creamos el entorno virtual:

	$ virtualenv -p /usr/bin/python3 flask

Para activar nuestro entorno virtual:

	$ source flask/bin/activate
	(flask)$ 

Y a continuación instalamos Flask:

	(flask)$ pip install Flask


Al finalizar podemos comprobar los paquetes python instalados:

	(flask)$ pip freeze
	Flask==0.12.2
	Jinja2==2.9.6
	MarkupSafe==1.0
	Werkzeug==0.12.2
	click==6.7
	itsdangerous==0.24

Y finalmente comprobamos la versión de flask que tenemos instalada:

	(flask)$ flask --version
	Flask 0.12.2
	Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
	[GCC 4.9.1]

## Corriendo una aplicación sencilla

Escribimos nuestra primera aplicación flask, en un fichero `app.py`:

	from flask import Flask
	app = Flask(__name__)	

	@app.route('/')
	def hello_world():
	    return '<h1>Hello, World!</h1>'

	if __name__ == '__main__':
   		app.run()

1. El objeto `app` de la clase Flask es nuestra aplicación WSGI, que nos permitirá posteriormente desplegar nuestra aplicación en un servidor Web. Se le pasa como parámetro el módulo actual (`__name__`).
2. El decorador `router` nos permite filtrar la petición HTTP recibida, de tal forma que si la petición se realiza a la URL `/` se ejecutará la función **vista** `hello_word`.
3. La función **vista** que se ejecuta devuelve una respuesta HTTP. En este caso devuelve una cadena de caracteres que se será los datos de la respuesta.
4. Finalmente si ejecutamos este módulo se ejecuta el método `run` que ejecuta un servidor web para que podamos probar la aplicación.

De esta forma podemos ejecutar nuestra primera aplicación:

	$ python3 app.py
	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Y podemos acceder a la URL `http://127.0.0.1:5000/` desde nuestro navegador.

# Enrutamiento: rutas

El objeto Flask `app` nos proporciona un decorador `router` que es capaz de filtrar la función *vista* que se va ejecutar analizando la petición HTTP, fundamentalmente por la ruta y el método que se hace la petición.

## Trabajando con rutas

Veamos un ejemplo:

	...
	@app.route('/')
	def hello_world():
	    return '<h1>Hello, World!</h1>'	

	@app.route('/articulos/')
	def articulos():
	    return '<h1>Lista de artículos</h1>'	

	@app.route('/acercade')
	def acercade():
	    return '<h1>Página acerca de...<h1>'

En este caso se comprueba la ruta de la petición HTTP, y cuando coincide con alguna indicada en las rutas se ejecuta la función correspondiente devolviendo una respuesta HTTP. 

Si declaramos rutas terminando en `/` son consideradas como un directorio de un sistema de fichero, en este caso si se accede a la ruta sin la barra final se producirá una redirección a la ruta correcta.

Si declaramos la rutas sin `/` final, se consideran un fichero del sistema de fichero, si accedemos a la ruta con el `/` nos devolverá una respuesta con código 404.

Si la ruta de la petición HTTP no corresponde con ninguna que hayamos indicado se devolverá una respuesta con código de estado 404 indicando que no se ha encontrado el recurso.

### Rutas dinámicas

Podemos gestionar rutas variables, es decir que correspondan a un determinado patrón o expresión regular, por ejemplo:

	@app.route("/articulos/<int:id>")
	def mostrar_ariculo(id):
		return 'Vamos a mostrar el artículo con id:{}'.format(id)

	