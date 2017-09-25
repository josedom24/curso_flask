from flask import Flask, render_template, abort
app = Flask(__name__)	

@app.route('/hola/<nombre>')
def saluda(nombre):
    return render_template("template1.html",nombre=nombre)


@app.route('/suma/<num1>/<num2>')
def suma(num1,num2):
	try:
		resultado=int(num1)+int(num2)
	except:
		abort(404)
	return render_template("template2.html",num1=num1,num2=num2,resultado=resultado)

@app.route('/tabla/<numero>')
def tabla(numero):
	try:
		numero=int(numero)
	except:
		abort(404)
	return render_template("template3.html",num=numero)

@app.route('/enlaces')
def enlaces():
	enlaces=[{"url":"http://www.google.es","texto":"Google"},
			{"url":"http://www.twitter.com","texto":"Twitter"},
			{"url":"http://www.facbook.com","texto":"Facebook"},
			]
	return render_template("template4.html",enlaces=enlaces)


@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

