# Generando formularios con flask-wtf

[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) es una extensión de Flask que nos permite trabajar con la librería [WTForm](https://wtforms.readthedocs.io/en/latest/) de python, que nos permite generar y validar formulario HTML de una forma sencilla.

## Instalación de Flask-WTF

Con nuestro entorno virtual ejecutamos:

	pip install Flask-WTF

Por dependencia se instal la librería WTForm.

## Trabajando formularios generado con WTForm

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

Como puedes ver hemos creado una clase heredada de la clase [`Form`](https://wtforms.readthedocs.io/en/latest/forms.html) donde hemos indicado distintos atributos que son objetos de los distitos [tipos de campos](https://wtforms.readthedocs.io/en/latest/fields.html) que podemos indicar, donde inicializamos distinos datos (label, [validaciones](https://wtforms.readthedocs.io/en/latest/validators.html),...).

En nuestra aplicación tenemos que importar la clase que hemos creado:

	from aplicacion.forms import formcalculadora




