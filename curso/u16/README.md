# Herencia de plantillas

La herencia de plantillas nos permite hacer un esqueleto de plantilla, para que todas las páginas de nuestro sitio web sean similares. En la unidad anterior hicimos una plantilla independiente para cada página, eso tiene un problema: si queremos cambiar algo que se común a todas las páginas hay que cambiarlo en todos los ficheros.

En nuestro caso vamos a crear una plantilla base de donde se van a heredar todas las demás e indicaremos los bloques que hay las plantillas hijas pueden sobreescribir.

## La plantilla base

Vamos a crear una plantilla `base.html` donde indicaremos las partes comunes de todas nuestras páginas, e indicaremos los bloques que las otras plantillas pueden reescribir.

	<!DOCTYPE html>
	<html lang="es">
	<head>
	<title>{% block title %}{% endblock %}</title>
	<link rel="stylesheet" href="{{url_for("static", filename='css/style.css')}}">
	<meta charset="utf-8" />
	</head>
	 
	<body>
	    <header>
	       <h1>Mi sitio web</h1>
	       <p>Mi sitio web creado en html5</p>
	    </header>
	    {% block content %}{% endblock %}
	</body>
	</html>

Algunas consideraciones:

1. Hemos creado dos bloques (`title` y `content`) en las plantillas hijas vamos a poder rescribir esos dos bloque para poner el título de la página y el contenido. Podríamos indicar todos los bloques que necesitamos.
2. Hemos incluido una hoja de estilo que está en nuestro contenido estático (directorio `static`)

## Herencia de plantillas

A continuación, veamos la primera plantilla (`tample1.html`) utilizando la técnica de herencia:

	{% extends "base.html" %}
	{% block title %}Hola, que tal {{nombre}}{% endblock %}
	{% block content %}
	    <h2>Vamos a saludar</h2>
	    {% if nombre %}
	      <h1>Hola {{nombre|title}}</h1>
	      <p>¿Cómo estás?</p>
	    {%else%}
	      <p>No has indicado un nombre</p>
	    {% endif %}
	{% endblock %}

Observamos cómo hemos reescrito los dos bloques.

Ejecuta el programa y comprueba que se genera el documento HTML completo, comprueba también que se está usando una hoja de estilo.

Puedes ver el diseño de las demás plantillas en el código ejemplo.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u16)