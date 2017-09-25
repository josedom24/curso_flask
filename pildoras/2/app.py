from flask import Flask, request,url_for
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
    return  '<a href="{}">Sumar</a>'.format(url_for("sumar"))

@app.route("/suma",methods=["GET","POST"])
def sumar():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		return "El resultado es {}".format(str(int(num1)+int(num2)))
	else:
		return '''<form action="/suma" method="POST">
				<label>N1:</label>
				<input type="text" name="num1"/>
				<label>N2:</label>
				<input type="text" name="num2"/>
                <input type="submit"/>
				</form>'''

if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
