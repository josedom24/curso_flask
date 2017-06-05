# Trabajando con formularios

La manera más usual de enviar información a las distintas páginas de nuestra aplicación web es usando [formularios HTML5](https://www.w3schools.com/html/html_forms.asp). Es recomendable utilizar el método POST (la información se envía en el cuerpo de la petición) para el envio de información usando formularios, aunque si es necesario también podemos usar el ḿétodo GET (la información se envía en la URL de la petición).

## Ejemplo de calculadora

En el código ejemplo de esta unidad hemos desarrollado una calculadora, en una plantilla creamos un formulario donde se piden dos números y un operador,según el operador se muestra el resultado.

## Calculadora con POST

Como hemos indicado anteriormente al enviar la información con un formulario se manda con el método POST. Cuando accedemos la primera vez a la ruta `/calculadora_post` lo estamos haciendo usando el método GET por lo tanto nos devuelve una plantilla donde mostramos el formulario:

	<form action={{url_for("calculadora_post")}} method="post">
		
		Número1: <input type="text" name="num1" autofocus required />
		<br />
		Número2: <input type="text" name="num2" autofocus required />
		<br />
		Operación: 
		<select name="operador">
  			<option value="+">Suma</option>
  			<option value="-">Resta</option>
  			<option value="*">Multiplicación</option>
  			<option value="/">División</option>
  		</select> 
  		<br/>
  		<input type="submit" value="Submit!" />
	</form>

Mandamos tres datos: `num1`, `num2` y `operador` a la misma ruta `/calculadora_post` pero en esta ocasión se utilzia el método POST, en este caso se lee los datos del formulario, se calcula la operación y se muetra una plantilla con el resultado:

	@app.route("/calculadora_post", methods=["get","post"])
	def calculadora_post():
		if request.method=="POST":
			num1=request.form.get("num1")
			num2=request.form.get("num2")
			operador=request.form.get("operador")
		
			try:
				resultado=eval(num1+operador+num2)
			except:
				return render_template("error.html",error="No puedo realizar la operación")
			
			return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
		else:
			return render_template("calculadora_post.html")

## Calculadora con GET

No es habitual pero vemos el mismo programa pero en este caso enviando la información del formulario con el método GET. En este caso al acceder a la ruta `/calculadora_get` tenemos que determinar si es la primera vez que hemos accedido, para ello comprobamos si la URL tiene algún argumento (`len(request.args)>0`) sino tiene argumentos mostramos una plantilla con el formulario, igual que en la anterior excepto en la definición del formualrio:

	<form action={{url_for("calculadora_get")}} method="get">
	...

Si la çURL tiene parámetros (`len(request.args)>0`) llemos los parámetros y realizamos la operación, sería similar al programa anterior, lo que cambia es cómo se leen los parámetros de la URL:

	...
	num1=request.args.get("num1")
	num2=request.args.get("num2")
	operador=request.args.get("operador")
	...

## Utiliza rutas dinámicas

Cuando se envía información con formularios debemos usar el método POST, si vamos a mandar información en la URL deberíamos usar rutas dinámicas:

	@app.route("/calculadora/<operador>/<num1>/<num2>", methods=["get"])
	def calculadora_var(operador,num1,num2):
		...

## Formulario completo

En otro ejercicio del código ejemplo, puedes comprobar que hemos realizado un formulario con muchos tipos de campos, cómo hemos leido esa información y la hemos envíado a una plantilla para mostralos. (¡¡¡Comprueba en el código la contraseña que tienes que introducir para que el programa funcione!!!)

## Código ejemplo de esta unidad

[Código](../../ejemplos/u18)
	