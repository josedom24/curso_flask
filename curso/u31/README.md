# Uso de cookies para añadir artículos al carrito

Las cookie son información que el navegador guarda en memoria o en el disco duro dentro de ficheros texto, a solicitud del servidor.

## Manejo de cokies en flask

En flask tenemos que generar una respuesta HTTP que solicite la creación de una cookie en el cliente, para crear una cookie habrá qe indicar un nombre y el valor (cadena de caracteres) que se guarda. De forma generar:

	@app.route('/set_cookie')
	def cookie_insertion():
	    redirect_to_index = redirect('/index')
	    response = current_app.make_response(redirect_to_index )  
	    response.set_cookie('cookie_name',value='values')
	    return response

En este caso realizamos una redirección guardando una cookie en el navegador.

Para leer la información de una cokkie utilizaremos la siguiente intrucción:

	datos = request.cookies.get('cookie_name')

## Creación del carrito de compra con cookies

En nuetro ejemplo vamos a guardar los datos del carrito de la compra en una cookie.Cuando compremos un videojuego vamos a indicar la cantidad que vamos a comprar, y si hay suficiente stock se guardará dicha información en la cookie.

Vamos a utilizar JSON como lenguaje de marcas para guardar la información de los articulos que vamos añadiendo al carrito, de tal manera vamos a gurdar una lista con los identificadores y la cantidad de cada artículo que vamos a comprar y el nombre que le vamos a dar a la cookie será el identificardor del usuario que está realizando la compra. Por ejemplo, el usuario con id 1 ha comprado dos artículos:

	datos=[{"cantidad": 1, "id": "1"}, {"cantidad": 2, "id": "2"}]"

Si volvemos a seleccionar un artículo que está en el carrito previamente y cambiamos la cantidad habrá que actualizar el contenido de la cookie, de la misma manera que si borramos un artículo del carrito.

En python el manejo de datos JSON se hace con tipos de datos lista y diccionarios, como en la cokkie hay que guardar una cadena de caracteres, utilizaremos la siguiente función del módulo son`para convertir la ista de diccionarios en cadena de caracteres:

	json.dumps(datos)

Por ejemplo para crear una cookie con los datos de los articulos:

	resp.set_cookie(str(current_user.id),json.dumps(datos))

De forma similar cuando leemos la información de la cookie que es una cadena de caracteres y la queremos convertir a listas  y diccionarios, utilizaremos la siguiente función:

	json.loads(cadena)

Por lo tanto para leer la información de la cookie:

	datos = json.loads(request.cookies.get(str(current_user.id)))

