# Generando respuestas HTTP, respuestas de error y redirecciones

El decorador `router` gestiona la petición HTTP recibida y crea un objeto `reponse` con la respuesta HTTP: el código de estado, las cabaceras y los datos devueltos. Esta respuesta la prepara a partir de lo que devuelve la función *vista* ejecutada con cada `route`. Estas funciones pueden devolver tres tipos de datos:

* Una cadena, o la generación de una plantilla (que veremos posteriormente). Por defecto se indica un código 200 y las cabeceras por defecto.
* Un objeto de la clase `response` generado con la función `make_repsonse`, que recibe los datos devueltos, el código de estado y las cabeceras.
* Una tupla con los mismos datos: datos, cabeceras y código de respuesta.

## Ejemplo de respuestas

Veamos el siguiente código:

	@app.route('/string/')
	def return_string():
	    return 'Hello, world!'	

	@app.route('/object/')
	def return_object():
	    headers = {'Content-Type': 'text/plain'}
	    return make_response('Hello, world!', 200,headers)	

	@app.route('/tuple/')
	def return_tuple():
	    return 'Hello, world!', 200, {'Content-Type':'text/plain'}

Puedes comprobar que devuelve cada una de las rutas.

{% include "../../adsense.md" %}

## Respuestas de error

Si queremos que en cualquier momento devolver una respuesta HTTP de error podemos utilizar la función `abort`:

	@app.route('/login')
	def login():
    	abort(401)
    	# Esta línea no se ejecuta

Y lo comprobamos:

	curl  http://localhost:5000/login	

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
	<title>401 Unauthorized</title>
	<h1>Unauthorized</h1>
	<p>The server could not verify that you are authorized to access the URL requested.  You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.</p>

Si queremos responder de la misma manera un determinado código de estado, por ejemplo queremos devolver una respuesta determinada cuando no se encuentra un recurso:

	@app.errorhandler(404)
	def page_not_found(error):
	    return 'Página no encontrada...', 404

	curl  http://localhost:5000/login2 
	Página no encontrada...

## Redirecciones

Si queremos realizar una redicirección HTTP a otra URL utilizamos la función `redirect`:

	@app.route('/')
	def index():
	    return redirect(url_for('return_string'))

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u12)

{% include "../../adsense2.md" %}