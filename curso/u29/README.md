# Gestión de permisos de usuarios

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

