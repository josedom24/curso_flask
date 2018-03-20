# Introducción a flask

Flask es un "micro" framework escrito en Python y concebido para facilitar el desarrollo de aplicaciones Web bajo el patrón MVC.

## ¿Qué es un framework?

Podemos definir framework como un esquema (un esqueleto, un patrón) para el desarrollo y/o la implementación de una aplicación. En general los framework están asociado a lenguajes de programación (Ruby on Rails (Ruby), Symphony (PHP),...).

Las ventajas tiene utilizar un ‘framework’ pueden ser:

* El programador no necesita plantearse una estructura global de la aplicación, sino que el framework le proporciona un esqueleto que hay que "rellenar".
* Facilita la colaboración. Cualquiera que haya tenido que "pelearse" con el código fuente de otro programador sabrá lo difícil que es entenderlo y modificarlo; por tanto, todo lo que sea definir y estandarizar va a ahorrar tiempo y trabajo a los desarrollos colaborativos.
* Es más fácil encontrar herramientas (utilidades, librerías) adaptadas al framework concreto para facilitar el desarrollo.

Después de estudiar la unidad: [Introducción a la programación web con python](../u4) llegamos a la conclusión de que es necesario de utilizar un framework para ayudarnos a gestionar las peticiones y generar las respuestas correspondientes. Si utilizamos python como lenguaje de programación web tenemos a nuestra disposición un conjunto de framework: [Web Frameworks for Python](https://wiki.python.org/moin/WebFrameworks).

{% include "../../adsense3.md" %}

## ¿Por qué usar flask?

* Flask es un "micro" framework: se enfoca en proporcionar lo mínimo necesario para que puedas poner a funcionar una aplicación básica en cuestión de minutos. Se necesitamos más funcionalidades podemos extenderlo con las [Flask extensions](http://flask.pocoo.org/extensions/).
* Incluye un servidor web de desarrollo para que puedas probar tus aplicaciones sin tener que instalar un servidor web.
* También trae un depurador y soporte integrado para pruebas unitarias. 
* Es compatible con python3, por lo tanto podemos usar la codificación de caracteres unicode, y 100% compatible con el estándar WSGI.
* Buen manejo de rutas: Con el uso de un decorador python podemos hacer que nuestra aplicación con URL simples y limpias.
* Flask soporta el uso de cookies seguras y el uso de sesiones.
* Flask se apoya en el motor de plantillas Jinja2, que nos permite de forma sencilla renderizar vistas y respuestas.
* Flask no tiene ORMs, wrappers o configuraciones complejas, eso lo convierte en un candidato ideal para aplicaciones ágiles o que no necesiten manejar ninguna dependencia. Si necesitas trabajar con base de datos sólo tenemos que utilizar una extensión.
* Este framework resulta ideal para construir servicios web (como APIs REST) o aplicaciones de contenido estático.
* Flask es Open Source y está amparado bajo una licencia BSD.
* Puedes ver el código en [Github](https://github.com/pallets/flask), la [documentación](https://github.com/pallets/flask) es muy completa y te puedes suscribir a su [lista de correos](http://flask.pocoo.org/mailinglist/) para mantenerte al día de las actualizaciones.

## Extensiones flask

Ya hemos visto la [lista de extensiones](http://flask.pocoo.org/extensions/) que nos permite ampliar la funcionalidad de Flask, en este curso vamos a utilizar las siguientes:

* `Flask-Script`: La extensión flask-script nos proporciona la posibilidad de gestionar nuestra aplicación flask desde una comando (Interfaz de línea de comando).
* `Flask-Bootstrap`: si queremos trabajar con plantillas que utilicen como hoja de estilos y javascript el framework bootstrap podemos ulizar la extansión Flask-Bootstrap.
* `Flask-WTF`: Flask-WTF es una extensión de Flask que nos permite trabajar con la librería WTForm de python, que nos facilita la generación y validación de formularios HTML.
* `Flask-Sqlalchemy`: Usaremos la extensión Flask-SQLAlchemy que nos provee un wrapper para el proyecto SQLAlchemy, el cual es un Object Relational Mapper o ORM.
* `Flask-Login`: Flask-Login es una librería que nos proporciona la posibilidad de gestionar las sesiones de nuestros usuarios.

{% include "../../adsense2.md" %}