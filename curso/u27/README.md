In [1]: from aplicacion.app import db

In [2]: from aplicacion.models import Usuarios

In [3]: u=Usuarios()

In [4]: u.nombre="pepe"

In [5]: u.password="asdasd"

In [6]: u.username="pepe"

In [7]: u.email="a@a.es"

In [8]: db.session.add(u)

In [9]: db.session.commit()

In [12]: u.password_hash
Out[12]: 'pbkdf2:sha256:50000$EFhxMbr1$ea8e6ddeaaac8d73d01f78f1b3d3120184cc25aea9491e632b4fc8c9ae2705cb'

