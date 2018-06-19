import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Client(Base):
	__tablename__ = 'client'
	id = Column(Integer, primary_key=True)
	name = Column(String(256), nullable=False)
	ip_address = Column(String(64), nullable=False)

class Dataset(Base):
	__tablename__ = 'dataset'
	id = Column(Integer, primary_key=True)
	filename = Column(String(64), nullable=False)
	client_id = Column(Integer, ForeignKey('client.id'))
	client = relationship(Client)
    
engine = create_engine('sqlite:///data.db')

Base.metadata.create_all(engine)
