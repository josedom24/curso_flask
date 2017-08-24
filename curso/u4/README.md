# Introducción a la programación web con python

Aunque de forma general se utilizan distintos framework (por ejemplo Flask) para el desarrollo de aplicaciones web con Python. En este artículo voy a introducir los conceptos necesarios para crear una página web desarrollada con python sin utilizar ningún framework. Para ello es necesario conocer el concepto de WSGI Web Server Gateway Interface, que es una especificación de una interface simple y universal entre los servidores web y las aplicaciones web o frameworks desarrolladas con python.

## Creación de la aplicación WSGI

Todas las peticiones que hagamos a nuestro servidor estarán manejadas por la aplicación WSGI, que será un único fichero. Esta aplicación será la responsable de manejar las peticiones, y de devolver la respuesta adecuada según la URI solicitada. En esta aplicación tendremos que definir una función, que actúe con cada petición del usuario. Esta función, deberá ser una función WSGI aplicación válida. Esto significa que:

* Deberá llamarse `application`.
* Deberá recibir dos parámetros: `environ`, del módulo `os`, que provee un diccionario de las peticiones HTTP estándar y otras variables de entorno, y la función `start_response`, de WSGI, encargada de entregar la respuesta HTTP al usuario.

Veamos el primer ejemplo `wsgi1.py`:

	# -*- coding: utf-8 -*-
	def application(environ, start_response):
	    # Guardo la salida que devolveré como respuesta
	    respuesta = "<p>Página web construida con <strong>Python!!!</strong></p>"
	    # Se genera una respuesta al navegador 
	    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	    return respuesta	

	if __name__ == '__main__':
	    from wsgiref.simple_server import make_server
	    srv = make_server('localhost', 8080, application)
	    srv.serve_forever()

Para ejecutar este programa ejecutamos:

	$ python wsgi1.py

Se creará un servidor web que responderá en `localhost` en el puerto `8080`.

## Creando una aplicación web un "poco más compleja"

El controlador que hemos hecho anteriormente no tiene en cuenta la URL con la que hemos accedido al servidor y siempre va a generar la misma respuesta. Utilizando la información sobre la petición que tenemos guardada en el diccionario `environ` podemos construir diferentes respuestas según la petición, por ejemplo teniendo en cuenta la URL de acceso.

El diccionario `environ` que se recibe con cada pedido HTTP, contiene las variables estándar de la especificación CGI, entre ellas:

* `REQUEST_METHOD`: método "GET", "POST", ...
* `SCRIPT_NAME`: la parte inicial de la "ruta", que corresponde a la aplicación
* `PATH_INFO`: la segunda parte de la "ruta", determina la "ubicación" virtual dentro de la aplicación.
* `QUERY_STRING`: la porción de la URL que sigue al "?", si existe
* `CONTENT_TYPE`, `CONTENT_LENGTH` de la petición HTTP
* `SERVER_NAME`, `SERVER_PORT`, que combinadas con `SCRIPT_NAME` y `PATH_INFO` dan la URL
* `SERVER_PROTOCOL`: la versión del protocolo ("HTTP/1.0" or "HTTP/1.1")

De esta forma podemos hacer un controlador (fichero `wsgi2.py`) de la siguiente manera, para comprobar la URL de acceso:

	# -*- coding: utf-8 -*-
	def application(environ, start_response):
	    if environ["PATH_INFO"]=="/":
	        respuesta = "<p>Página inicial</p>"
	    elif environ["PATH_INFO"]=="/hola":
	        respuesta = "<p>Bienvenidos a mi página web</p>"
	    else:
	        respuesta = "<p><trong>Página incorrecta</strong></p>"
	    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	    return respuesta	

	if __name__ == '__main__':
	    from wsgiref.simple_server import make_server
	    srv = make_server('localhost', 8080, application)
	    srv.serve_forever()

En este último ejemplo (fichero `wsgi3.py`) vamos a ver cómo podemos trabajar con parámetros enviados por el método GET:

	# -*- coding: utf-8 -*-
	def application(environ, start_response):
	    if environ["PATH_INFO"]=="/":
	        respuesta = "<p>Página inicial</p>"
	    elif environ["PATH_INFO"]=="/suma":
	        params=environ["QUERY_STRING"].split("&")
	        suma=0
	        for par in params:
	                suma=suma+int(par.split("=")[1])
	        respuesta="<p>La suma es %d</p>" % suma
	    else:
	        respuesta = "<p><trong>Página incorrecta</strong></p>"
	    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	    return respuesta	

	if __name__ == '__main__':
	    from wsgiref.simple_server import make_server
	    srv = make_server('localhost', 8080, application)
	    srv.serve_forever()

## Código ejemplo de esta unidad

[Código](../../ejemplos/u4)