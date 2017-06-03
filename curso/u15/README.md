	# Plantillas con jinja2

[Jinja2](http://jinja.pocoo.org) es un motor de plantilla desarrollado en Python. Flask utiliza el sistema de plantillas de jinja2 para generar documentos HTML válidos de una manera muy sencilla y eficiente.

Por dependencias al instalar Flask instalamos jinja2. en esta unidad vamos a estudiar los elementos principales de jinja2, para más información accede la [documentación](http://jinja.pocoo.org/docs).

## Una plantilla simple

Veamos un ejemplo para entender como funcion jinja2:

	from jinja2 import Template

	temp1="Hola {{nombre}}"
	print(Template(temp1).render(nombre="Pepe"))

La salida es `Hola Pepe`. La plantilla se compone de una variable `{{nombre}}` que es sustituida por el valor de la variable `ǹombre` al renderizar o generar la plantilla.

## Elementos de una plantilla

Una plantilla puede esta formada por texto, y algunos de los siguientes elementos:

* Variables, se indican con {{ ... }}
* Instrucciones, se indican com {% ... %}
* Comentarios, se indican con {# ... #}

## 