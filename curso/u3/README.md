# Patrón modelo-vista-controlador

Modelo–vista–controlador (MVC) es un patrón de arquitectura de software, que separa los datos y la lógica de negocio de una aplicación de la interfaz de usuario y el módulo encargado de gestionar los eventos y las comunicaciones. Para ello MVC propone la construcción de tres componentes distintos que son el modelo, la vista y el controlador.

* El Modelo: Es la representación de la información con la cual el sistema opera, por lo tanto gestiona todos los accesos a dicha información, tanto consultas como actualizaciones, implementando también los privilegios de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio).
* El Controlador: Responde a eventos (usualmente acciones del usuario) e invoca peticiones al 'modelo' cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos). También puede enviar comandos a su 'vista' asociada si se solicita un cambio en la forma en que se presenta el 'modelo', por tanto se podría decir que el 'controlador' hace de intermediario entre la 'vista' y el 'modelo'.
* La Vista: Presenta el 'modelo' (información y lógica de negocio) en un formato adecuado para interactuar (usualmente la interfaz de usuario) por tanto requiere de dicho 'modelo' la información que debe representar como salida.

## Flask y MVC

Flask es totalmente compatible con el patrón MVC:

* Aunque por defecto no tiene un ORM, podemos usar una extensión de Flask para definir el modelo de datos. Esta característica nos abstrae del uso del motor de Base de Datos y lo hace independiente.
* Con Flask vamos a definir un controlador, que es capaz de determinar las rutas con las que accedemos a la aplicación, procesar la información necesaria y mostrar la información necesaria en cada momento.
* Flask utiliza jinja2 como motor de plantillas, con lo que es muy fácil diseñar las vistas que vamos a mostrar a los usuarios en cada momento.