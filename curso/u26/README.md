# Borrando un registro de la base de datos

En este apartado vamos a estudiar como borrar un registro en nuestra base de datos.

## Modificando artículos

## Modificación en el modelo de datos

Vamos a modificar nuestro modelo de datos, para indicar que vamos a borrar en cascada en nuestra relación, es decir al borrar una categoría vamos a borrar todos los videojuegos de esa categoría, para ello en el fichero `models.py` cambiamos la siguiente línea en el ódelo `Categorias`:

	articulos = relationship("Articulos", cascade="all, delete-orphan", backref="Categorias",lazy='dynamic')

Tenemos que volver a generar la base de datos para que tenga efecto este cambio.

## Borrando artículos

Lo primero es insertar un enlace en la página principal que nos permita borrar artículos (se añade un enlace por cada artículo), para ello en la plantilla `inicio.html`:

	<td><a href="{{url_for('articulos_delete',id=art.id)}}"><span class="glyphicon glyphicon-trash"></span> Borrar</a></td>

* Vamos a usar un formulaeio (`formSINO`) para confirmar que queremos borrar una artículo. Este formulario, simplemente nos ofrece dos botones (Sí o No) para confirmar el borrado. En el fichero `forms.py`:

		class formSINO(FlaskForm):      
			si = SubmitField('Si') 
			no = SubmitField('No') 

* Utilizamos el template `articulos_delete.html` para mostrar el formulario.
* En el programa principal, vamos a crear una ruta dinámica, que nos permite borrar un registro según su identificador:

		@app.route('/articulos/<id>/delete', methods=["get","post"])

* Lo primero que hacemos es seleccionar el artículo según el identificador recibido en la ruta, sino existe el artículo devolvemos un error:

		art=Articulos.query.get(id)
			if art is None:
				abort(404)

* Creamos un nuevo formulario. Este formulario va a recibir la información que hemos introducido y envado por el métiodo POST y la información del fichero que hemos subido, sin embargo al entrar por primera vez (método GET) se va a rellenar con lo datos del objeto `Articulos` que hemos seleccionado:

		form=formArticulo(obj=art)

* Si en el formulario pulsamo "Si":
		
		form=formSINO()
		if form.validate_on_submit():
			if form.si.data:
				if art.image!="":
					os.remove(app.root_path+"/static/upload/"+art.image)
				db.session.delete(art)
				db.session.commit()
			return redirect(url_for("inicio"))
		return render_template("articulos_delete.html",form=form,art=art)

	Se realizan las siguientes acciones:

	* Borramos el fichero de la imagen correspondiente, si tenía una imagen asociada..
	* Se borra el objeto `Articulos` que hemos seleccionado.
* Si el formulario no es válido o hemos pulsado "No" volvemos a la página principal.

## Borrando categorías

De una forma similar puedes estudiar el código para ver cómo se borran las categorías en nuestra base de datos. Comprueba que al borrar una categoría se borran todos los videojuegos asociados.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u26)