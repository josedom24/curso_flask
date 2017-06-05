from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from aplicacion.forms import formcalculadora
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")


@app.route("/procesar", methods=["post"])
def procesar_formulario():
	passwd=request.form.get("pass_control")
	if passwd=="asdasd":
		datos = request.form
		return render_template("datos.html",datos=datos)	
	else:
		return render_template("error.html",error="Contraseña incorrecta")

@app.route("/calculadora_post", methods=["get","post"])
def calculadora_post():
	form=formcalculadora(request.form)
	if form.validate_on_submit():
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		operador=request.form.get("operador")
	
		try:
			resultado=eval(num1+operador+num2)
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		
		return render_template("calculadora_post.html",form=form)		




@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)
