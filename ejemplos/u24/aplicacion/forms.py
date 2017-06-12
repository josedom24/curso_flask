from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class formCategoria(FlaskForm):                      
	nombre=StringField("Nombre:",validators=[Required("Tienes que introducir el dato")])
	submit = SubmitField('Enviar')

