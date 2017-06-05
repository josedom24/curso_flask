from flask_wtf import FlaskForm
from wtforms import Form, IntegerField,SelectField,SubmitField
from wtforms.validators import Required


class formcalculadora(FlaskForm):                      
	num1=IntegerField("Número1",validators=[Required("Tienes que introducir el dato")])
	num2=IntegerField("Número2",validators=[Required("Tienes que introducir el dato")])
	operador=SelectField("Operador",choices=[("+","Sumar"),("-","Resta"),
											("*","Multiplicar"),("/","Dividir")])
	submit = SubmitField('Submit')

