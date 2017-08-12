# Gestión de permisos de usuarios

En esta unidad vamos a estudiar como autorizar las distintas acciones que pueden hacer nuestro usuarios en la aplicación. Cuando accedemos a la aplicación podemos hacerlo de tres formas distintas:

* Usuario invitado: Navegamos por la página sin autentificar ningún usuario del sistema.
* Usuario normal: Nos hemos autentificado con un usuario que no es administrador.
* Usuario administrador: Nos hemos autentificado con un usuario administrador.

## Control de acceso

Veamos una tabla donde indicamos según el tipo de usuario con el que estamos trabajnfo las distintas acciones que se pueden realizar:

| Acción   | Invitado | Normal | Administrador |
| :------- | :------: | :----: | :-----------: |
| Hacer login | Si | No | No |
| Registrarse | Si | No | No |


Que estás logueado:

if session["id"]

Que eres admin:

if session["admin"]

Permisos

Usuario no logueado:

* Puede hacer login
* Puede registrarse
* No puede ver perfil
* No puede cambiar contraseña
* Puede ver videojuegos
* Puede ver categorias
* No puede modificar, borrar, comprar videojuegos
* No puede modificar, borrar categorias


Usuarios logueados:

* No puede hacer login
* No puede registrarse
* Puede ver perfil
* Puede cambiar contraseña
* Puede ver videojuegos
* Puede ver categorias
* Puede comprar videojuegos
* No puede modificar, borrar videojuegos
* No puede modificar, borrar categorias

Usuario administrador

* No puede hacer login
* No puede registrarse
* Puede ver perfil
* Puede cambiar contraseña
* Puede ver videojuegos
* Puede ver categorias
* Puede comprar videojuegos
* Puede modificar, borrar videojuegos
* Puede modificar, borrar categorias

