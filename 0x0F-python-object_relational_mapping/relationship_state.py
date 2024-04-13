#!/usr/bin/python3
""" Module that defines the State class using SQLAlchemy,
    where City is defined as a relationship
"""

from relationship_city import Base, City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """Represents a State for a MySQL database.

    Attributes:
        __tablename__ (str): name of the table
        id: Represents a column of an auto-generated, unique integer,
            can't be null and is a primary key
        name: Represent a column of a string with 128 maximum characters
            and can't be null
        cities: Represents a column of string relationship
    """
    
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", bakref="state")
