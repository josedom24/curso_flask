# Registrando nuevos usuarios

En esta unidad vamos a estudiar como un usuario se puede registrar en nuestra aplicación, y una vez registrado podrá cambiar los datos de su perfil. En realidad lo que estamos haciendo es creando y modificando registros en la tabla de usuarios.

## Registro de nuevos usuarios

En la plantilla `base.html` hemos introducido un enlace para el registro de nuevos usuarios (si no hay un usuario logueado) y para acceder al perfil (si el usuario está logueado):

	{% if session["id"] %}
          <a class="navbar-brand " href="/perfil/{{ session["username"]}}"> Perfil</a>
          <a class="navbar-brand " href="/logout"> {{ session["username"]}} (Salir)</a>
    {% else %}
          <a class="navbar-brand " href="/login">Login</a>
          <a class="navbar-brand " href="/registro">Registro</a>
    {% endif %}

En el programa principal hemos creado una ruta `registro` que nos permite mostrar el formulario de registro, si los datos introducidos son válidos (el usuario indicado no existe en la base de datos) se crea un nuevo usuario:

	@app.route("/registro",methods=["get","post"])
	def registro():
		form=formUsuario()
		if form.validate_on_submit():
			existe_usuario=Usuarios.query.filter_by(username=form.username.data).first()
			if existe_usuario==None:
				user=Usuarios()
				form.populate_obj(user)
				user.admin=False
				db.session.add(user)
				db.session.commit()
				return redirect(url_for("inicio"))
			form.username.errors.append("Nombre de usuario ya existe.")
		return render_template("usuarios_new.html",form=form)

El formulario utilizado para crear el nuevo usuario se llama `formUsuario` y lo puedes ver en el fichero `forms.py`. 

## Modificación de los datos de un usuario (perfil)

El usuario puede modificar sus datos accediendo a la ruta `perfil`. Utilizamos el mismo formulario `formUsuario`, pero la plantilla que lo visualiza (`usuarios_new.html`) muestra elementos diferentes según sea el registro o el perfil:

* Si estamos registrando un nuevo usuario muestra un cuadro de texto para introducir el nombre de usuario, si estamos en el perfil muestra el mismo cuadro de texto pero en modo sólo lectura, para simplificar el proceso:

		{% if not perfil %}
          {{form.username.label() }}{{form.username(size="100",class="form-control")}}<br/>
        {% else %}
          {{form.username.label() }}{{form.username(readonly="readonly",size="100",class="form-control")}}<br/>
        {% endif %} 

* Si estamos registrando un nuevo usuario muestra un cuadro de texto para introducir la contraseña, si estamos en el perfil muestra un enlace para cambiar la contraseña:

		{% if not perfil %}
          {{form.password.label() }}{{form.password(size="100",class="form-control")}}<br/>
        {% else %}
          <a href="/changepassword/{{session["username"]}}">Cambiar contraseña</a><br/>
        {% endif %}

La ruta `perfil` muetra el formulario y cambia los datos que modifiquemos, menos la contraseña:

	@app.route('/perfil/<username>', methods=["get","post"])
	def perfil(username):
		user=Usuarios.query.filter_by(username=username).first()
		if user is None:
			abort(404)	

		form=formUsuario(request.form,obj=user)
		del form.password	
		if form.validate_on_submit():
			form.populate_obj(user)
			db.session.commit()
			return redirect(url_for("inicio"))	

		return render_template("usuarios_new.html",form=form,perfil=True)

## Cambio de contraseña

Un usuario registrado también puede cambiar su contraseña, pero lo hemos realizado en una plantilla independiente (`changepassword.html`) y un formulario `formChangePassword`. Para realizar el cambio de contraseña hemos creado la ruta `changepassword`:

	@app.route('/changepassword/<username>', methods=["get","post"])
	def changepassword(username):
		user=Usuarios.query.filter_by(username=username).first()
		if user is None:
			abort(404)	

		form=formChangePassword()
		if form.validate_on_submit():
			form.populate_obj(user)
			db.session.commit()
			return redirect(url_for("inicio"))	

		return render_template("changepassword.html",form=form)

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u28)