import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    favorites = relationship("Favorite", backref = "user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Planet(Base): 
    __tablename__="planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    favorites = relationship("Favorite", backref = "planet")


    def serialize(self):
        return {     
            "name": self.name,
            "id": self.id,
        }

class Characters(Base): 
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    favorites = relationship("Favorite", backref = "characters")

    def serialize(self):
        return {     
            "name": self.name,
        }
class Favorite(Base):
    __tablename__="favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    def serialize(self):
        people = People.get_by_id(self.people_id)
        return {
            "id": self.id,
            "user_id": self.user_id,
            "pcharacters_id": self.characters_id,
            "planet_id": self.planet_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')