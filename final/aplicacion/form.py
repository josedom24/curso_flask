from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, FloatField, IntegerField
from wtforms.validators import Length, required

class ArticulosForm(FlaskForm):
	nombre = TextField('Nombre', [Length(max=100),required()])
	precio = FloatField('Precio')
	iva = IntegerField('IVA')
	description = TextAreaField('Descripcion')
	stock = IntegerField('IVA')