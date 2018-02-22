# Generando formularios con flask-wtf

[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) es una extensión de Flask que nos permite trabajar con la librería [WTForm](https://wtforms.readthedocs.io/en/latest/) de python, que nos facilita la generación y validación de formularios HTML.

## Instalación de Flask-WTF

Con nuestro entorno virtual ejecutamos:

	pip install Flask-WTF

Por dependencia se instala la librería WTForm.

## Creando formularios

En el directorio de nuestra aplicación (`aplicacion`) vamos a crear un fichero (`forms.py`) donde vamos a guardar los distintos formularios de nuestra aplicación. Por ejemplo el fichero `forms.py`:

	from flask_wtf import FlaskForm
	from wtforms import Form, IntegerField,SelectField,SubmitField
	from wtforms.validators import Required	
	

	class formcalculadora(FlaskForm):                      
		num1=IntegerField("Número1",validators=[Required("Tienes que introducir el dato")])
		num2=IntegerField("Número2",validators=[Required("Tienes que introducir el dato")])
		operador=SelectField("Operador",choices=[("+","Sumar"),("-","Resta"),
								("*","Multiplicar"),("/","Dividir")])
		submit = SubmitField('Submit')

Como puedes ver hemos creado una clase heredada de la clase [`FlaskForm`](https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms) donde hemos indicado distintos atributos que son objetos de los distintos [tipos de campos](https://wtforms.readthedocs.io/en/latest/fields.html) que podemos indicar, donde inicializamos distintos datos (label, [validaciones](https://wtforms.readthedocs.io/en/latest/validators.html),...).

## Trabajando con formularios

En nuestra aplicación tenemos que importar la clase que hemos creado:

	from aplicacion.forms import formcalculadora

Y a continuación podemos crear un objeto a partir de ella:

	form = formcalculadora()

Al crear el formulario podemos inicialzarlos con datos, normalmente con los parámetros recibidos en la vista (`request.form`):

	form = formcalculadora(request.form)	

El objeto `form` nos ofrece algunos atributos y métodos para su gestión:

* `form.validate_on_submit()`: Nos permite comprobar si el formulario ha sido enviado y es válido.
* `form.data`: Nos ofrece un diccionario con los datos del formulario.
* `form.errors`: Si el formulario no es válido nos devuelve un diccionario con los errores.
* `form.num1.data`: Para cada campo (en este ejemplo `num1`)`nos devuelve su valor.
* `form.num1.errors`: Es una tupla con los errores de validación de el campo determinado.
* `form.num1()`: Nos devuelve el código HTML para generar este campo.
* `form.num1.label()`: Nos devuelve el código HTML para general la etiqueta del campo.

Puedes encontrar más atributos y métodos en la [documentación de WTForm](https://wtforms.readthedocs.io/en/latest/).

## Seguridad en los formularios

Por defecto Flask-WTF protege los formularios contra el ataque CSRF (Cross-Site Request Forgery o [falsificación de petición en sitios cruzados](https://es.wikipedia.org/wiki/Cross-site_request_forgery)). Este ataque se produce cuando un sitio web malicioso envía solicitudes a un sitio web en el que está conectada la víctima.

Para implementar la protección CSRF, Flask-WTF necesita que configuremos una clave de cifrado, para generar tokens encriptados que se utilizarán para verificar la autenticidad de la petición. Para ello, en nuestro programa principal:

	app.secret_key = 'clave de cifrado lo más robusta posible'

Cada vez que generemos un formulario se incluirá un campo oculto que contendrá el token cifrado que permitirá verificar que el envió del formulario ha sido lícita. Para generar este campo oculto utilizamos el método `form.csrf_token()` que mostrará un código HTML parecido a este:

	<input id="csrf_token" name="csrf_token" type="hidden" value="IjE5OWRiYmY0MGE2MT...">

## Generación de formularios

En nuestra plantillas, podemos generar el formulario campo por campo, por ejemplo:

	
	{% raw %}<form action={{url_for("calculadora_post")}} method="post">{% endraw %}
	    {{ form.csrf_token }}
		{{form.num1.label() }}{{form.num1()}}<br/>
		{{form.num2.label() }}{{form.num2()}}<br/>
		{{form.operador.label() }}{{form.operador()}}<br/>
  		{% raw %}<br/>{% endraw %}
  		{{form.submit()}}
	</form>

También tenemos la opción de recorrer el formulario:

	<form action={{url_for("calculadora_post")}} method="post">    
	    {% for field in form %}
	    	{{field.label() }}{{field()}}<br/>
	    {% endfor %}
	</form>

Para mostrar los errores de validación podemos realizar un recorrido similar a este:

	{% for field, errors in form.errors.items() %}
		<div class="alert alert-danger">
    		{{ form[field].label }}: {{ ', '.join(errors) }}
		</div>
	{% endfor %}

## Enviando y gestionando la información del formulario

Vamos a usar un [patrón de diseño](http://flask.pocoo.org/docs/0.12/patterns/wtforms/) basado en la creación de una vista que se comporte de la siguiente manera:

1. La primera vez que accedemos a la ruta accedemos utilizando el método GET. En nuestro caso se creará un formulario sin datos (ya que `request.form` no tiene ningún dato) , el formulario no se ha enviado y por lo tanto se devuelve la plantilla con el formulario vacío.
2. Se rellena el formulario y se manda la información a la misma ruta pero utilizando el método POST. En este caso se crea un formulario que se rellena con la información que se ha recibido del formulario.
3. Si el formulario es válido se gestiona la información y se realiza la acción que se tenga que hacer (guardar en una base  de datos, mostrar una plantilla resultado,...)
4. Si el formulario no es válido se vuelve a generar la plantilla con el formulario con datos, mostrando si lo hemos codificado los errores de validación oportunos.

En nuestro caso la vista que hemos puesto en nuestro ejemplo de la calculadora quedaría de la siguiente manera:

	@app.route("/calculadora_post", methods=["get","post"])
	def calculadora_post():
		form=formcalculadora(request.form)
		if form.validate_on_submit():
			num1=form.num1.data
			num2=form.num2.data
			operador=form.operador.data
			try:
				resultado=eval(str(num1)+operador+str(num2))
			except:
				return render_template("error.html",error="No puedo realizar la operación")
			
			return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
		else:
			
			return render_template("calculadora_post.html",form=form)		

## Código ejemplo de esta unidad

[Código](../../ejemplos/u19)
	