# Gestión de usuarios con sesiones

En esta unidad vamos a introducir el concpto de sesión para posibilitar que los usuarios de nuetra página puedan loguearse en ella. Posteriormente veremos como autorizar el acceso a las distintas opciones de nutra aplicación según el role del usuario. En esta unidad vamos a trabjar directamente con sesiones, en una unidad posterior utilizarmos la extensión de Flask `flask-login` para realizar la autentificación.

## El modelo de datos para guardar los usuarios

Necesitamos una nueva tabla en nuetra base de datos para guardar los usuarios, para ello en nuestro modelo de datos (fichero `models.py`) añadimos la clase `Usuarios`:

	class Usuarios(db.Model):
		"""Usuarios"""
		__tablename__ = 'usuarios'
		id = Column(Integer, primary_key=True)
		username = Column(String(100),nullable=False)
		password_hash = Column(String(128),nullable=False)
		nombre = Column(String(200),nullable=False)
		email = Column(String(200),nullable=False)
		admin = Column(Boolean, default=False)
		
		def __repr__(self):
			return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))	

		@property
		def password(self):
			raise AttributeError('password is not a readable attribute')	

		@password.setter
		def password(self, password):
			self.password_hash = generate_password_hash(password)
		def verify_password(self, password):
			return check_password_hash(self.password_hash, password)

Algunas indicaciones interesantes:

* Los datos de usuario se van a gaurdar en una tabla llamada `usuarios`.
* Guardamos un identificador, un nombre de usuario, contraseña (que estará cifrada), el nombre, el correo electrónico y un valor lógico (admin) que nos indica si el usuario es adminitrador. Vamos a tener dos roles de usuarios; administradores y usuarios normales.
* Tenemos una propiedad `password`. Al intentar obtener su valor, nos devuelve una excepción indicado que no se puede leer, si intentamos modificarla, lo que realmente se hace es cifrarla en el atributo `password_hash` con la función `generate_password_hash` del módulo `werkzeug.security`.
* También tneemos un método `verify_password` que utilizando la función `check_password_hash` del módulo `werkzeug.security`, nos permite verificar si la contraseña guarda es igual a la indicada como parámetro.

Tenemos que volver a generar las tablas para tener a nuetra disposición el nuevo modelo. Una vez realizada esta operación podemos hacer una prueba, creando un usuario:

	>>> from aplicacion.app import db
	>>> from aplicacion.models import Usuarios
	>>> u=Usuarios()
	>>> u.nombre="pepe"
	>>> u.password="asdasd"
	>>> u.username="pepe"
	>>> u.email="a@a.es"
	>>> db.session.add(u)
	>>> db.session.commit()
	>>> u.password_hash
	>>> 'pbkdf2:sha256:50000$EFhxMbr1$ea8e6ddeaaac8d73d01f78f1b3d3120184cc25aea9491e632b4fc8c9ae2705cb'
	>>> u.password
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_flask/ejemplos/u27/aplicacion/models.py", line 53, in password
	    raise AttributeError('password is not a readable attribute')
	AttributeError: password is not a readable attribute

## Creación del usuario administrador

Para facilitar la creación de un primer usuario con role administrados hemos introducido una nuev funcionalidad en nuestro manejador `manage.py`:

	@manager.command
	def create_admin():
	    usuario={"username":input("Usuario:"),
	            "password":getpass("Password:"),
	            "nombre":input("Nombre completo:"),
	            "email":input("Email:"),
	            "admin": True}
	    usu=Usuarios(**usuario)
	    db.session.add(usu)
	    db.session.commit()

Que nos pide los datos del usuario ppor teclado y crea un usuarioa administrador:

	$ python3 manage.py create_admin
	Usuario:
	...

## Autentficando usuarios en nuestra aplicación

Una vez que tenemos preparado nuetro modelo de datos y utilizando sesiones vamos a programar la posibilidad de que un usuario se autentifique en nuestra aplicación y simulemos una sesión en ella hasta que salga del sistema. Para ello vamos a realizar los siguientes pasos:

* El formulario `LoginForm` nos va posibilitar pedir nombre de usuario y contraseña para verificar si es un usuario correcto, por lo tanto en el fichero `forms.py`:

		class LoginForm(FlaskForm):
			username = StringField('Login', validators=[Required()])
			password = PasswordField('Password', validators=[Required()])
			submit = SubmitField('Entrar')

* Flask nos permite trabajar con sesiones, hemos creado un fichero `login.py` con el siguiente contenido:

		def login_user(Usuario):
			session["id"]=Usuario.id
			session["username"]=Usuario.username
			session["admin"]=Usuario.admin		

		def logout_user():
			session.pop("id",None)
			session.pop("username",None)
			session.pop("admin",None)

	Cuando un usuario se haya logueado de manera adecuada, utilizaremos la función `login_user` para crearvariables de sesiones con la información del identificador, el nombre de usuario y su rol. si el usuario sale del sistema se utilizará la función `logout_user` para borrar dichas variables y terminar la sesión.

* Por lo tanto si existe alguna de las variables `session` tendremos un usuario logueado en el sistema. Esta variable es accesible desde las plantillas, por lo tanto en la plantilla `base.html` podemos introducir el siguiente código:

		{% if session["id"] %}
          <a class="navbar-brand " href="/logout"> Hola, {{ session["username"]}} (Salir)</a>
        {% else %}
          <a class="navbar-brand " href="/login">Login</a>
        {% endif %}

    Si existe la variable `session["id"]` tenemos un usuario en el sistema: ponemos su nombre de usuario y un enlace a "Salir". Si esa variable no existe ponemos un enlace para posibilitar que el usuario introduzca sus credenciales.

* En el programa principal, creamos una ruta `login` que muetra el formulario de login, si mandamos el formulario con éxito busca el usuario en la base de datos y comprueba la contraseña indicada si todo es correcto crea la sesión con la función `login_user()`:

		@app.route('/login', methods=['get', 'post'])
		def login():
		    form = LoginForm()
		    if form.validate_on_submit():
		    	user=Usuarios.query.filter_by(username=form.username.data).first()
		    	if user!=None and user.verify_password(form.password.data):
		    		login_user(user)
		    		return redirect(url_for('inicio'))
		    	
		    	form.username.errors.append("Usuario o contraseña incorrectas.")
		    return render_template('login.html', form=form)

* También hemos creado una ruta `logout` que nos permite al usuario terminar la sesión utilizando la función `logout_user():

		@app.route("/logout")
		def logout():
			logout_user()
			return redirect(url_for('login'))

En la siguiente unidad veremos como autorizar las distintas operaciones que puede realizar un usuario según su rol.

## Código ejemplo de esta unidad

[Código](../../ejemplos/u27)