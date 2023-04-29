import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name =Column(String)

class Favorites(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'favorites'
    user_id =Column(Integer,ForeignKey('user.id'))
    basic_data_id =Column(Integer,ForeignKey('basic_data.id'))


class BasicData(Base):
    __tablename__ = 'basic_data'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String)

class  character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    Gender = Column(String)
    hair_color =Column(String)
    eye_color = Column(String)
    basic_data_id = Column (Integer,ForeignKey('basic_data.id'),primary_key=True)

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,primary_key=True)
    population = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'),primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
