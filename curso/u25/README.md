# Modificando registros en la base de datos

En este apartado vamos a estudiar como modificar un registro en nuestra base de datos.

## Modificando artículos

Lo primero es insertar un enlace en la página principal que nos permita modificar artículos (se añade un enlace por cada artículo), para ello en la plantilla `inicio.html`:

	<td><a href="{{url_for('articulos_edit',id=art.id)}}"><span class="glyphicon glyphicon-pencil"></span> Modificar</a></td>

* Vamos a usar el mismo formulario (`formArticulo`) que hemos utilizado en la unidad anterior para añadir nuevos artículos, para realizar la modificación.
* Vamos a utilizar el mismo template `articulos_new.html` para mostrar el formulario.
* En el programa principal, vamos a crear una ruta dinámica, que nos permite modificar un registro según su identificador:

		@app.route('/articulos/<id>/edit', methods=["get","post"])

* Lo primero que hacemos es seleccionar el artículo según el identificador recibido en la ruta, sino existe el artículo devolvemos un error:

		art=Articulos.query.get(id)
			if art is None:
				abort(404)

* Creamos un nuevo formulario. Este formulario va a recibir la información que hemos introducido y enviado por el método POST y la información del fichero que hemos subido, sin embargo al entrar por primera vez (método GET) se va a rellenar con lo datos del objeto `Articulos` que hemos seleccionado:

		form=formArticulo(obj=art)

{% include "../../adsense3.md" %}

* Si el formulario es válido:
		
		...
		if form.validate_on_submit():
			#Borramos la imagen anterior
			if  form.photo.data:
				os.remove(app.root_path+"/static/upload/"+art.image)
				try:
					f = form.photo.data
					nombre_fichero=secure_filename(f.filename)
					f.save(app.root_path+"/static/upload/"+nombre_fichero)
				except:
					nombre_fichero=""
			else:
				nombre_fichero=art.image
			
			form.populate_obj(art)
			art.image=nombre_fichero
			db.session.commit()
			return redirect(url_for("inicio"))

	Se realizan las siguientes acciones:

	* Si hemos subido otra imagen se elimina la anterior.
	* Se intenta guardar el fichero que se ha subido en el formulario.
	* Si no se ha subido ninguno el nombre la imagen sigue siendo la anterior.
	* Se modifica el objeto `Articulos` al rellenar con los datos del formulario (`form.populate_obj(art)`).
* Si el formulario no es válido se vuelve a generar la plantilla con el formulario con datos, mostrando si lo hemos codificado los errores de validación oportunos.

## Modificando categorías

De una forma similar puedes estudiar el código para ver cómo se modifican las categorías en nuestra base de datos.

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u25)

{% include "../../adsense2.md" %}