# Trabajando con peticiones HTTP

Hemos indicado que nuestra aplicación Flask recibe una petición HTTP, cuando la URL a la que accedemos se corresponde con una ruta y un método indicada en una determinada `route` se ejecuta la función correspondiente. Desde esta función se puede acceder al objeto `request` que posee toda la información de la petición HTTP.

## El objeto request

Veamos los atributos más importante que nos ofrece el objeto `request`:

	@app.route('/info',methods=["GET","POST"])
	def inicio():
	    cad=""
	    cad+="URL:"+request.url+"\n"
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


* `request.url`: La URL a la que accedemos.
* `request.path`: La ruta de la URL, quitamos el servidor y los parámetros con información.
* `request.method`: El método HTTP con el qué hemos accedido.
* `request.headers`: Las cabeceras de la petición HTTP. Tenemos atributos para acceder a cabeceras en concreto, por ejemplo, `request.user_agent`.
* `request.form`: Información recibida en el cuerpo de la petición cuando se utiliza el método POST, normalmente se utiliza un formulario HTML para enviar esta información.
* `request.args`: Parámetros con información indicado en la URL en las peticiones GET.
* `request.files`: Ficheros para subir al servidor en una petición PUT o POST.

Flask usa un tipo especial de diccionario `ImmutableMultiDict` en algunos de sus atributos (headers, form, args, files) en el que se puede guaradar varios valores por cada clave.

Ejemplos:

	curl http://localhost:5000/info
	URL:http://localhost:5000/info
	PATH:/info
	Método:GET
	header:
	User-Agent:curl/7.38.0
	Accept:*/*
	Host:localhost:5000
	información en formularios (POST):
	información en URL (GET):

	curl http://localhost:5000/info\?id\=100

	...
	información en URL (GET):
	id:100

	curl -X POST http://localhost:5000/info -d id=100

	...
	Método:POST
	header:
	Content-Type:application/x-www-form-urlencoded
	Content-Length:6
	información en formularios (POST):
	id:100

## Ejemplo: sumar dos números

	@app.route("/suma",methods=["GET","POST"])
	def sumar():
		if request.method=="POST":
			num1=request.form.get("num1")
			num2=request.form.get("num2")
			return str(int(num1)+int(num2))
		else:
			return '''<from action="/suma" method="POST">
					<label>N1:</label>
					<input type="text" name="num1"/>
					<label>N2:</label>
					<input type="text" name="num2"/>
					</form>'''

Cuando accedemos la primera vez a la URL accedemos con el método GET, y nos muestra el formulario:

	curl http://localhost:5000/suma
	
	<from action="/suma" method="POST">
		<label>N1:</label>
	...

Cuando introducimos dos números, se mandan a la misma URL con el método POST por lo que nos da el resultado de la suma:

	curl -X POST http://localhost:5000/suma -d num1=6 -d num2=8 
	14

## Código ejemplo de esta unidad

[Código](../../ejemplos/u11)

