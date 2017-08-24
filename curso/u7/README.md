# Corriendo una aplicación sencilla

Escribimos nuestra primera aplicación flask, en un fichero `app.py`:

	from flask import Flask
	app = Flask(__name__)	

	@app.route('/')
	def hello_world():
	    return 'Hello, World!'

	if __name__ == '__main__':
   		app.run()

1. El objeto `app` de la clase Flask es nuestra aplicación WSGI, que nos permitirá posteriormente desplegar nuestra aplicación en un servidor Web. Se le pasa como parámetro el módulo actual (`__name__`).
2. El decorador `router` nos permite filtrar la petición HTTP recibida, de tal forma que si la petición se realiza a la URL `/` se ejecutará la función **vista** `hello_word`.
3. La función **vista** que se ejecuta devuelve una respuesta HTTP. En este caso devuelve una cadena de caracteres que se será los datos de la respuesta.
4. Finalmente si ejecutamos este módulo se ejecuta el método `run` que ejecuta un servidor web para que podamos probar la aplicación.

De esta forma podemos ejecutar nuestra primera aplicación:

	$ python3 app.py
	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Y podemos acceder a la URL `http://127.0.0.1:5000/` desde nuestro navegador y ver el resultado. O podemos ejecutar:

	$curl http://127.0.0.1:5000
	Hello, World!

## Configuración del servidor web de desarrollo

Podemos cambiar la dirección y el puerto desde donde nuestro servidor web va a responder. Por ejemplo si queremos acceder a nuestra aplicación desde cualquier dirección en el puerto 8080:

	...
	app.run('0.0.0.0',8080)

	$ python3 app.py
	* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)


## Modo "debug"

Si activamos este modo durante el proceso de desarrollo de nuestra aplicación tendremos a nuestra disposición una herramienta de depuración que nos permitirá estudiar los posibles errores cometidos, además se activa el modo "reload" que inicia automáticamente el servidor de desarrollo cuando sea necesario. Para activar este modo:

	...
	app.run(debug=True)

	$ python3 app.py
	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	* Restarting with stat
	* Debugger is active!
	* Debugger PIN: 106-669-497

El `Debugger PIN` lo utilizaremos para utilizar la herramienta de depuración.


## Código ejemplo de esta unidad

[Código](../../ejemplos/u7)
