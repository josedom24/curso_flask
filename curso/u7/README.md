# Corriendo una aplicación sencilla

Escribimos nuestra prinmera aplicación flask, en un fichero `app.py`:

	from flask import Flask, run
	app = Flask(__name__)	

	@app.route('/')
	def hello_world():
	    return 'Hello, World!'

	if __name__ == '__main__':
   		app.run()

1. El objeto `app` de la clase Flask es nuestra aplicación WSGI, que nos permitirá posteriormente desplegar nuestra aplicación en un servidor Web. Se le pasa como párametro el módulo actual (`__name__`).
2. El decorador `router` nos permite filtrar la petición HTTP recibida, de tal forma que si la petición se realiza a la URL `/` se ejecutará la función *vista* `hello_word`.
3. La función *vista* que se ejecuta devuelve una respuesta HTTP. En este caso devuelve una cadena de caracteres que se será los datos de la respuesta.
4. Finalmente si ejecutamos este módulo se ejecuta el método `run` que ejecuta un servidor web para que podamos probar la aplicación.




