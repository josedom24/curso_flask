from flask import Flask, request,url_for,render_template
from lxml import etree
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	doc=etree.parse("sevilla.xml")
	municipios=doc.findall("municipio")
	return render_template("inicio.html",municipios=municipios)

@app.route('/<code>')
def temperatura(code):
	doc=etree.parse("http://www.aemet.es/xml/municipios/localidad_"+code+".xml")
	name=doc.find("nombre").text
	max=doc.find("prediccion/dia/temperatura").find("maxima").text
	min=doc.find("prediccion/dia/temperatura").find("minima").text
	return render_template("temperaturas.html",name=name,max=max,min=min)

if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
