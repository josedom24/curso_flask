from datetime import datetime
from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Categorias(Base):
	"""Categorías de los artículos"""
	__tablename__ = 'categorias'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100))
	


	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Articulos(Base):
	"""Artículos de nuestra tienda"""
	__tablename__ = 'articulos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100),nullable=False)
	precio = Column(Float,default=0)
	iva = Column(Integer,default=21)
	descripcion = Column(String(255))
	image = Column(String(255))
	stock = Column(Integer,default=0)
	CategoriaId=Column(Integer,ForeignKey('categorias.id'), nullable=False)
	categoria = relationship("Categorias", backref="Articulos")

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))



class Usuarios(Base):
	"""Usuarios"""
	__tablename__ = 'usuarios'
	id = Column(Integer, primary_key=True)
	username = Column(String(200),nullable=False)
	password = Column(String(200),nullable=False)
	nombre = Column(String(200),nullable=False)
	fecha =  Column(DateTime, nullable=False)
	activo = Column(Boolean, default=False)
	email = Column(String(200),nullable=False)
	admin = Column(Boolean, default=False)

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

if __name__ == '__main__':  # pragma: no cover
    from datetime import timedelta
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///../dbase.db', echo=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    categorias = ("Deportes","Arcade","Carreras","Acción")

    for cat in categorias:
    	categoria=Categorias(nombre=cat)
    	session.add(categoria)
    	session.commit()

    juegos=[
    {"nombre":"Fifa 2017","precio":65,"descripcion":"juego de futbol","stock":10,"CategoriaId":1},
    {"nombre":"PES 2017","precio":35,"descripcion":"juego de futbol","stock":7,"CategoriaId":1},
    {"nombre":"PAC-MAN","precio":12,"descripcion":"juego de fantasmitas","stock":1,"CategoriaId":2},
    {"nombre":"Super Mario Bros","precio":25,"descripcion":"juego de plataforma","stock":5,"CategoriaId":2},
    {"nombre":"Need for Spped","precio":25,"descripcion":"juego de carreras","stock":10,"CategoriaId":3},
    {"nombre":"Out Run","precio":15,"descripcion":"juego de coches","stock":3,"CategoriaId":3},
    {"nombre":"Destiny","precio":75,"descripcion":"juego de disparos y acción","stock":8,"CategoriaId":4},
    {"nombre":"Metal Gear","precio":65,"descripcion":"juego de acción","stock":10,"CategoriaId":4},
    
    ]
    for jue in juegos:
       	juego=Articulos(**jue)
       	session.add(juego)
       	session.commit()
