# Subida de ficheros

Es posible realizar subidas de ficheros al servidor, Flask nos ofrece está [posibilidad](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/), pero vamos a utilizar la extensión Flask-WTF para facilitar esta labor. Hay que recordad que cuando se manda un fichero al servidor la información del fichero la encontramos en `request.file`.

En esta unidad vamos a hacer una aplicación web que nos permita generar una galería de imágenes. En nuestra galería vamos a poder subir imágenes a través de un formulario.

## Creando un formulario para subir ficheros

Vamos a utilizar el tipo de campo `FileField` para crear nuestro formulario para subir un fichero.

	from flask_wtf import FlaskForm
	from wtforms import SubmitField
	from flask_wtf.file import FileField, FileRequired	
	

	class UploadForm(FlaskForm):
	    photo = FileField('selecciona imagen:',validators=[FileRequired()])
	    submit = SubmitField('Submit')

Además hemos introducido una validación, indicando que es necesario indicar un fichero.

## Generando el formulario

De forma similar a lo que vimos en la unidad anterior vamos a generar el formulario en nuestra plantilla:

	<form action="{{url_for('upload')}}" method="POST" enctype="multipart/form-data">
    	{{ form.csrf_token }}
    	{{form.photo.label() }}{{form.photo()}}<br/>
		<br/>
  		{{form.submit()}}
	</form>

Al subir un fichero es necesario poner el atributo `enctype="multipart/form-data"` al definir el formulario.

## Tratamiento del fichero subido

Al crear la vista vamos a crear un formulario:

	form = UploadForm()

Al construir el objeto formulario no hemos indicado con que valores vamos a rellenar el formulario (en la unidad anterior lo indicábamos de esta manera: `form = UploadForm(request.form)`). cuando creamos un objeto de esta manera, automáticamente carga el formulario con los datos (`request.form`) y con los posibles ficheros que hayamos subido (`request.file`), por lo que tenemos a nuestra disposición los datos y los ficheros recibidos.

Si el formulario es válido:

* Creamos un objeto fichero a parir del formulario

		f = form.photo.data

* Creamos un nombre de fichero que sea compatible con el sistema de archivo (lo hacemos con la función `secure_filename`)

		filename = secure_filename(f.filename)

* Y lo guardamos en el directorio adecuado.

		f.save(app.root_path+"/static/img/"+filename)

* Finalmente realizamos una redirección al inicio de la página.

		return redirect(url_for('inicio'))

La vista completa quedaría de la siguiente manera:

	@app.route('/upload', methods=['get', 'post'])
	def upload():
		form= UploadForm() # carga request.from y request.file
		if form.validate_on_submit():
			f = form.photo.data
			filename = secure_filename(f.filename)
			f.save(app.root_path+"/static/img/"+filename)
			return redirect(url_for('inicio'))
		return render_template('upload.html', form=form)

## Código ejemplo de esta unidad

[Código](../../ejemplos/u20)