# Modificando registros en la base de datos

En este apartado vamos a estudiar como modificar un registro en nuestra base de datos.

## Modificando artículos

* Vamos el mismo formulario (`formArticulo`) que hemos utilizado en la unidad anterior para añadir nuevos artículos.
* Vamos a utilizar el mismo template `articulos_new.html` para mostrar el formulario.
* En el programa principal, vamos a crear una ruta dinámica, que nos permite modificar un registro según su identificador:

		@app.route('/articulos/<id>/edit', methods=["get","post"])

* Lo primero que hacemos es seleccionar el artículo según el identificador recibido en la ruta, sino existe el artículo devolvemos un error:

	art=Articulos.query.get(id)
		if art is None:
			abort(404)

* Creamos un nuevo formulario. Este formulario va a recibir la información que hemos introducido y envado por el métiodo POST y la información del fichero que hemos subido, sin embargo al entrar por primera vez (método GET) se va a rellenar con lo datos del objeto `Articulos` que hemos seleccionado:

		form=formArticulo(obj=art)

1. La primera vez que accedemos a la ruta accedemos utilizando el método GET. En nuestro caso se creará un formulario sin datos (ya que `request.form` no tiene ningún dato) , el formulario no se ha enviado y por lo tanto se devuelve la plantilla con el formulario vacío.
2. Se rellena el formulario y se manda la información a la misma ruta pero utilizando el método POST. En este caso se crea un formulario que se rellena con la información que se ha recibido del formulario (en el que añadimos la lista de categorías al campo `categorias`). 
3. Si el formulario es válido se gestiona la información y se realiza las siguientes acciones:
	* Se guarda el fichero que se ha subido el formulario.
	* Se crea un nuevo objeto `Articulos` y se rellena con los datos del formulario (`form.populate_obj(art)`).
4. Si el formulario no es válido se vuelve a generar la plantilla con el formulario con datos, mostrando si lo hemos codificado los errores de validación oportunos.

En la plantilla `articulos_new.html` puedes ver cómo se ha generado la página donde se muestra el formulario.

## Creando nuevas categorías

De una forma similar puedes estudiar el código para ver cómo se añaden nuevas categorías a nuestra base de datos.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u24)