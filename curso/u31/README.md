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

Para borrar una cookie lo haremos de la siguiente manera:

	response.set_cookie('cookie_name',value='',expires=0)

## Creación del carrito de compra con cookies

En nuetro ejemplo vamos a guardar los datos del carrito de la compra en una cookie.Cuando compremos un videojuego vamos a indicar la cantidad que vamos a comprar, y si hay suficiente stock se guardará dicha información en la cookie.

Vamos a utilizar JSON como lenguaje de marcas para guardar la información de los articulos que vamos añadiendo al carrito, de tal manera vamos a gurdar una lista con los identificadores y la cantidad de cada artículo que vamos a comprar y el nombre que le vamos a dar a la cookie será el identificardor del usuario que está realizando la compra. Por ejemplo, el usuario con id 1 ha comprado dos artículos:

	datos=[{"cantidad": 1, "id": "1"}, {"cantidad": 2, "id": "2"}]

Si volvemos a seleccionar un artículo que está en el carrito previamente y cambiamos la cantidad habrá que actualizar el contenido de la cookie, de la misma manera que si borramos un artículo del carrito.

En python el manejo de datos JSON se hace con tipos de datos lista y diccionarios, como en la cokkie hay que guardar una cadena de caracteres, utilizaremos la siguiente función del módulo son`para convertir la ista de diccionarios en cadena de caracteres:

	json.dumps(datos)

Por ejemplo para crear una cookie con los datos de los articulos:

	resp.set_cookie(str(current_user.id),json.dumps(datos))

De forma similar cuando leemos la información de la cookie que es una cadena de caracteres y la queremos convertir a listas  y diccionarios, utilizaremos la siguiente función:

	json.loads(cadena)

Por lo tanto para leer la información de la cookie:

	datos = json.loads(request.cookies.get(str(current_user.id)))

## Añadir artículos al carrito de la compra

Hemos creado una nueva ruta `/carrito/add/<id>` que recibe el identificador del artículo comprado (se ha añadido un enlace en el template `inicio.html`). Y realiza las siguiente acciones:

* Muestra el formulario `formCarrito` para indicar la cantidad de artículos que vamos a comprar.
* Si la cantidad indicada es menor que la cantidad de artículos que tenemos guardado en la base de datos, se lee la información anterior de la cookie.
* Ahora pueden pasar dos cosas: si el artículo ya existía en los datos de la cookie hay que actualizar el campo `cantidad` del diccionario, si el artículo no exite se añade un nuevo diccionario en la lista.
* Finalmente se crea una nueva cokkie con la información actualizada.

El código será el siguiente:

	@app.route('/carrito/add/<id>',methods=["get","post"])
	@login_required
	def carrito_add(id):
		art=Articulos.query.get(id)	
		form=formCarrito()
		form.id.data=id
		if form.validate_on_submit():
			if art.stock>=int(form.cantidad.data):
				try:
					datos = json.loads(request.cookies.get(str(current_user.id)))
				except:
					datos = []
				actualizar= False
				for dato in datos:
					if dato["id"]==id:
						dato["cantidad"]=form.cantidad.data
						actualizar = True
				if not actualizar:
					datos.append({"id":form.id.data,"cantidad":form.cantidad.data})
				resp = make_response(redirect(url_for('inicio')))
				resp.set_cookie(str(current_user.id),json.dumps(datos))
				return resp
			form.cantidad.errors.append("No hay artículos suficientes.")
		return render_template("carrito_add.html",form=form,art=art)

## Mostrar los artículos del carrito

Hemos creado una ruta `/carrito`, que nos muestra los artículos que hemos añadido al carrito. 

* Vamos a leer los datos de la cookie.
* Recorremos los diccionarios de la lista, y vamos guradando cada objeto `Articulos` y la cantidad de cada uno de ellos que vamos a comprar.
* Vamos acumulando El precio total de la compra.
* Finalmente mandamos esta información a la plantilla `carrito.html` para que muestre la información.

El código será el siguiente:

	@app.route('/carrito')
	@login_required
	def carrito():
		try:
			datos = json.loads(request.cookies.get(str(current_user.id)))
		except:
			datos = []
		articulos=[]
		cantidades=[]
		total=0
		for articulo in datos:
			articulos.append(Articulos.query.get(articulo["id"]))
			cantidades.append(articulo["cantidad"])
			total=total+Articulos.query.get(articulo["id"]).precio_final()*articulo["cantidad"]
		articulos=zip(articulos,cantidades)
		return render_template("carrito.html",articulos=articulos,total=total)

Por otro lado hemos creado una variable `num_articulos` en el contexto de las plantillas, para que podamos acceder al número de artículos que hay en el carrito desde las plantilla, para eso:

	@app.context_processor
	def contar_carrito():
		if not current_user.is_authenticated:
			return {'num_articulos':0}
		if request.cookies.get(str(current_user.id))==None:
			return {'num_articulos':0}
		else:
			datos = json.loads(request.cookies.get(str(current_user.id)))
			return {'num_articulos':len(datos)}

Y en la cabecera de la página, plantilla `base.html` hemos añadido un contado de artículos:

	<a class="navbar-brand " href="/carrito"> Carrito <span class="badge">{{num_articulos}} </span></a>

## Borrar artículos del carrito

Hemos añadido un enlace en la plantilla `carrito.html` que nos permite borrar un artículo del carrito. dicho enlace nos lleva a la ruta `/carrito_delete/<id>` que realizará las siguientes acciones:

* Vamos a leer los datos de la cookie.
* Para borrar el diccionario correspondiente al identidfcador que hemos recibido, vamos acrear otra lista sin dicho diccionario.
* Finalmente vamos a guardar en la cookie la nueva lista.

El código será el siguiente:

	@app.route('/carrito_delete/<id>')
	@login_required
	def carrito_delete(id):
		try:
			datos = json.loads(request.cookies.get(str(current_user.id)))
		except:
			datos = []
		new_datos=[]
		for dato in datos:
			if dato["id"]!=id:
				new_datos.append(dato)
		resp = make_response(redirect(url_for('carrito')))
		resp.set_cookie(str(current_user.id),json.dumps(new_datos))
		return resp

## Código ejemplo de esta unidad

[Código](../../ejemplos/u31)