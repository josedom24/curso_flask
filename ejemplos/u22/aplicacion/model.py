from datetime import datetime
from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from aplicacion.app import db


class Categorias(db.Model):
	"""Categorías de los artículos"""
	__tablename__ = 'categorias'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100))
	articulos = relationship("Articulos", backref="Categorias",lazy='dynamic')


	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Articulos(db.Model):
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

	def precio_final(self):
		return self.precio*self.iva/100

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))



class Usuarios(db.Model):
	"""Usuarios"""
	__tablename__ = 'usuarios'
	id = Column(Integer, primary_key=True)
	username = Column(String(100),nullable=False)
	password = Column(String(100),nullable=False)
	nombre = Column(String(200),nullable=False)
	fecha =  Column(DateTime)
	activo = Column(Boolean, default=False)
	email = Column(String(200),nullable=False)
	admin = Column(Boolean, default=False)
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

