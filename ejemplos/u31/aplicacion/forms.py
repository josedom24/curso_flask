from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,IntegerField,TextAreaField,SelectField,PasswordField, HiddenField, IntegerField
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField
from wtforms.validators import Required


class formCategoria(FlaskForm):                      
	nombre=StringField("Nombre:",validators=[Required("Tienes que introducir el dato")])
	submit = SubmitField('Enviar')


class formArticulo(FlaskForm):                      
	nombre=StringField("Nombre:",validators=[Required("Tienes que introducir el dato")])
	precio=DecimalField("Precio:",default=0,validators=[Required("Tienes que introducir el dato")])
	iva=IntegerField("IVA:",default=21,validators=[Required("Tienes que introducir el dato")])
	descripcion= TextAreaField("Descripción:")
	photo = FileField('Selecciona imagen:')
	stock=IntegerField("Stock:",default=1,validators=[Required("Tienes que introducir el dato")])
	CategoriaId=SelectField("Categoría:",coerce=int)
	submit = SubmitField('Enviar')

class formSINO(FlaskForm):      
	si = SubmitField('Si') 
	no = SubmitField('No') 

class LoginForm(FlaskForm):
	username = StringField('Login', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Entrar')

class formUsuario(FlaskForm):
	username = StringField('Login', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	nombre = StringField('Nombre completo')
	email = EmailField('Email')
	submit = SubmitField('Aceptar')	

class formChangePassword(FlaskForm):
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Aceptar')	

class formCarrito(FlaskForm):
	id = HiddenField()
	cantidad = IntegerField('Cantidad',default=1,validators=[Required("Tienes que introducir el dato")]))