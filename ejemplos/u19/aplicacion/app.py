from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from aplicacion.forms import formcalculadora
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():
    return render_template("inicio.html")


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




@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)
