# Creando registros en la base de datos

En este apartado vamos a estudiar como insertar un registro en nuestra base de datos.

## Creando nuevos artículos

Lo primero es insertar un enlace en la página principal que nos permita insertar nuevos artículos, para ello en la plantilla `inicio.html`:

	<a class="btn btn-primary" href="{{url_for('articulos_new')}}" role="button">Nuevo videojuego</a>

Para realizar nuestra operación vamos a crear un formulario que nos permite introducir los datos del nuevo artículo, para ello en el fichero `forms.py` creamos una nueva clase formulario con la siguiente sintaxis:

	class formArticulo(FlaskForm):                      
		nombre=StringField("Nombre:",validators=[Required("Tienes que introducir el dato")])
		precio=DecimalField("Precio:",default=0,validators=[Required("Tienes que introducir el dato")])
		iva=IntegerField("IVA:",default=21,validators=[Required("Tienes que introducir el dato")])
		descripcion= TextAreaField("Descripción:")
		photo = FileField('Selecciona imagen:')
		stock=IntegerField("Stock:",default=1,validators=[Required("Tienes que introducir el dato")])
		CategoriaId=SelectField("Categoría:",coerce=int)
		submit = SubmitField('Enviar')

Como novedad en el códigoo anterior hemos utilizado el atributo `coerce` del objeto `SelectField` que indica el tipo de datos que va a devolver, en este caso un entero que es el índice de las categorías.

En el programa principal hemos añadido una nueva ruta para añadir los nuevos artículos:

	@app.route('/articulos/new', methods=["get","post"])
	def articulos_new():
		form=formArticulo()
		categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
		form.CategoriaId.choices = categorias
		if form.validate_on_submit():
			try:
				f = form.photo.data
				nombre_fichero=secure_filename(f.filename)
				f.save(app.root_path+"/static/upload/"+nombre_fichero)
			except:
				nombre_fichero=""
			art=Articulos()
			form.populate_obj(art)
			art.image=nombre_fichero
			db.session.add(art)
			db.session.commit()
			return redirect(url_for("inicio"))
		else:
			return render_template("articulos_new.html",form=form)

Como habíamos visto en unidades anteriores:

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

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u24)