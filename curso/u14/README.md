# Plantillas con jinja2

[Jinja2](http://jinja.pocoo.org) es un motor de plantilla desarrollado en Python. Flask utiliza jinja2 para generar documentos HTML válidos de una manera muy sencilla y eficiente.

Por dependencias al instalar Flask instalamos jinja2. En esta unidad vamos a estudiar los elementos principales de jinja2, para más información accede a la [documentación oficial de jinja2](http://jinja.pocoo.org/docs).

## Una plantilla simple

Veamos un ejemplo para entender como funciona jinja2:

	from jinja2 import Template

	temp1="Hola {{nombre}}"
	print(Template(temp1).render(nombre="Pepe"))

La salida es `Hola Pepe`. La plantilla se compone de una variable `{{nombre}}` que es sustituida por el valor de la variable `nombre` al renderizar o generar la plantilla.

## Elementos de una plantilla

Una plantilla puede estar formada por texto, y algunos de los siguientes elementos:

* Variables, se indican con {% raw %}`{{ ... }}`{% endraw %}
* Instrucciones, se indican con {% raw %}`{% ... %}`{% endraw %}
* Comentarios, se indican con {% raw %}`{# ... #}`{% endraw %}

## Variables en las plantillas

Las variables en la plantillas se sustituyen por los valores que se pasan a la plantilla al renderizarlas. Si enviamos una lista o un diccionario puedo acceder los valores de dos maneras:

	{{ foo.bar }}
	{{ foo['bar'] }}

Veamos algunos ejemplos:

	temp2='<a href="{{ url }}"> {{ enlace }}</a>'
	print(Template(temp2).render(url="http://www.flask.com",enlace="Flask"))	

	temp3='<a href="{{ datos[0] }}"> {{ datos[1] }}</a>'
	print(Template(temp3).render(datos=["http://www.flask.com","Flask"]))	

	temp4='<a href="{{ datos.url }}"> {{ datos.enlace }}</a>'
	print(Template(temp4).render(datos={"url":"http://www.flask.com","enlace":"Flask"}))

El resultado de las tres plantillas es:

	<a href="http://www.flask.com"> Flask</a>

## Filtros de variables

Un filtro me permite modificar una variable. Son distintas funciones que me modifican o calculan valores a partir de las variables, se indican separadas de las variables por `|` y si tienen parámetros se indican entre paréntesis. Veamos algunos ejemplos:

	temp5='Hola {{nombre|striptags|title}}'
	print(Template(temp5).render(nombre="   pepe  "))	

	temp6="los datos son {{ lista|join(', ') }}"
	print(Template(temp6).render(lista=["amarillo","verde","rojo"]))	

	temp6="El ultimo elemento tiene {{ lista|last|length}} caracteres"
	print(Template(temp6).render(lista=["amarillo","verde","rojo"]))

Por defecto los caracteres (`>`, `<`, `&`, `"`) no se escapan, si queremos mostrarlo en nuestra página HTML tenemos que escapar los caracteres:

	temp7="La siguiente cadena muestra todos los caracteres: {{ info|e }}"
	print(Template(temp7).render(info="<hola&que&tal>"))

Y por tanto la salida es:

	La siguiente cadena muestra todos los caracteres: &lt;hola&amp;que&amp;tal&gt;

Para ver todos los filtros accede a la [lista de filtros](http://jinja.pocoo.org/docs/2.9/templates/#builtin-filters) en la documentación.

## Instrucciones en las plantillas

### for

Nos permite recorrer una secuencia, veamos un ejemplo sencillo. Es compatible con la sentencia `for` de python.

	temp7='''
	<ul>
	{% for elem in elems -%}
	<li>{{loop.index}} - {{ elem }}</li>
	{% endfor -%}
	</ul>
	'''
	print(Template(temp7).render(elems=["amarillo","verde","rojo"]))

La salida es:

	<ul>
	<li>1 - amarillo</li>
	<li>2 - verde</li>
	<li>3 - rojo</li>
	</ul>

El `-` detrás del bloque `for` evita que se añada una línea en blanco.

En un bloque `for` tenemos acceso a varias variables, veamos las más interesantes:

* `loop.index`: La iteración actual del bucle (empieza a contar desde 1).
* `loop.index0`: La iteración actual del bucle (empieza a contar desde 0).
* `loop.first`: True si estamos en la primera iteración.
* `loop.last`: True si estamos en la última iteración.
* `loop.length`: Número de iteraciones del bucle.

### if

Nos permite preguntar por el valor de una variable o si una variable existe. Es compatible con la sentencia `if` de python.

Ejemplo:

	temp9='''
	{% if elems %}
	<ul>
	{% for elem in elems -%}
		{% if elem is divisibleby 2 -%}
			<li>{{elem}} es divisible por 2.</li>
		{% else -%}
			<li>{{elem}} no es divisible por 2.</li>
		{% endif -%}
	{% endfor -%}
	</ul>
	{% endif %}
	'''
	print(Template(temp9).render(elems=[1,2,3,4]))

Y la salida será:

	<ul>
		<li>1 no es divisible por 2.</li>
		<li>2 es divisible por 2.</li>
		<li>3 no es divisible por 2.</li>
		<li>4 es divisible por 2.</li>
	</ul>

Tenemos un conjunto de tests para realizar comprobaciones, por ejemplo `divisibleby` devuelve True si un número es divible por el que indiquemos. Hay más tests que podemos utilizar. Para ver todos los tests accede a la [lista de tests](http://jinja.pocoo.org/docs/2.9/templates/#builtin-tests) en la documentación.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u14)