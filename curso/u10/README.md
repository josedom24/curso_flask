# Enrutamiento: Métodos

Para acceder a las distintas URLs podemos utilizar varios métodos en nuestra petición HTTP. En nuestros ejemplos vamos a trabajar con el método GET y POST, que son los métodos que normalmente podemos utilizar desde un navegador web.

* GET: Se realiza una petición para obtener un recurso del servidor web. Es el método más utilizado.
* POST: Aunque con el método GET también podemos mandar información al servidor (por medio de parámetros escritas en la URL), utilizamos el método POST para enviar información a una determinada URL. Normalmente utilizamos los formularios HTML para enviar información al servidor por medio del método POST:

Por defecto las rutas indicadas en la funciones `route` sólo son accesibles utilizando el método POST. Por ejemplo:

	$ curl -X POST http://localhost:5000/articulos/
	
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
	<title>405 Method Not Allowed</title>
	<h1>Method Not Allowed</h1>
	<p>The method is not allowed for the requested URL.</p>

Si una URL recibe información por medio del método POST y no queremos que se acceda a ella con un método GET, se definirá de la siguiente manera:

	@app.route('/articulos/new',methods=["POST"])
	def articulos_new():
		return 'Está URL recibe información de un formulario con el método POST'

Y por lo tanto:

	curl http://localhost:5000/articulos/new
	
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
	<title>405 Method Not Allowed</title>
	<h1>Method Not Allowed</h1>
	<p>The method is not allowed for the requested URL.</p>	

	curl -X POST http://localhost:5000/articulos/new
	
	Está URL recibe información de un formulario con el método POST       

También en muchas ocasiones es deseable acceder a una URL con los dos métodos, de tal manera que haremos una cosa cuando acedemos con GET y haremos otra cuando se acceda con POST. Ejemplo:

	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if request.method == 'POST':
	        return 'Hemos accedio con POST'
	    else:
	        return 'Hemos accedido con GET'

Y si accedemos:

	curl http://localhost:5000/login
	Hemos accedido con GET

	curl -X POST http://localhost:5000/login
	Hemos accedio con POST

En este ejemplo hemos utilizado el objeto `request` que estudiaremos en la siguiente unidad.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u10)