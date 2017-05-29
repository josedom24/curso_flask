from datetime import datetime
from sqlalchemy import Boolean, Column
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Articulos(Base):
	"""An appointment on the calendar."""
	__tablename__ = 'articulos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(255))
	precio = Column(Float)
	

