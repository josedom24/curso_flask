from flask import Flask, request
app = Flask(__name__)	

@app.route('/info',methods=["GET","POST"])
def inicio():
    cad=""
    cad+="URL:"+request.url+"\n"
    cad+="PATH:"+request.path+"\n"
    cad+="Método:"+request.method+"\n"
    
    cad+="header:\n"
    for item,value in request.headers.items():
    	cad+="{}:{}\n".format(item,value)

    cad+="información en formularios (POST):\n"
    for item,value in request.form.items():
    	cad+="{}:{}\n".format(item,value)
    
    cad+="información en URL (GET):\n"
    for item,value in request.args.items():
    	cad+="{}:{}\n".format(item,value)    
    
    cad+="Ficheros:\n"
    for item,value in request.files.items():
    	cad+="{}:{}\n".format(item,value)

    return cad

@app.route("/suma",methods=["GET","POST"])
def sumar():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		return str(int(num1)+int(num2))
	else:
		return '''<form action="/suma" method="POST">
				<label>N1:</label>
				<input type="text" name="num1"/>
				<label>N2:</label>
				<input type="text" name="num2"/>
                <input type="submit"/>
				</form>'''

