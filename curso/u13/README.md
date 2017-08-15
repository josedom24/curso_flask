# Contenido estático

Nuestra página web necesita tener contenido estático: hoja de estilo, ficheros java script, imágenes, documentos pdf, etc. Para acceder a eelos vamos a utilizar la función `url_for`.

## ¿Dónde guardamos el contnido estático?

Dentro de nuestro directorio `aplicacion` vamos a crear un directorio llamado `static`, donde podemos crear la estrucutra de directorios adecuada para guardas nuestro contenido estático. Por ejemplo para guardar el CSS, el java script y las imágenes podríamos crear una estrucutra como la siguiente:

	aplicacion
		static
			css
			js
			img
## Acceder al contenido estático

Por ejemplo:

	url_for('static', filename='css/style.css')

Estariamos creando la ruta para acceder al fichero `style.css` que se encuentra en `static/css`.

Otro ejemplo:

	url_for('static', filename='img/tux.png')

Estariamos creando la ruta para acceder al fichero `tux.png` que se encuentra en `static/img`.

## Mostrar una imagen

	@app.route('/')
	def inicio():
	    return '<img src="'+url_for('static', filename='img/tux.png')+'"/>'

Y comprobamos que se muestra al acceder a la página:

![imagen](img/img1.png)

## Código ejemplo de esta unidad

[Código](../../ejemplos/u13)
