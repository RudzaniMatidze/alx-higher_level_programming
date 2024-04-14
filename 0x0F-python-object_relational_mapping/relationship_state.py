#!/usr/bin/python3
"""Defines a state and Inherits from SQLAlchemy Base and
links to the MySQL table cities"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Class State

    Attributes:
        id: Represents a column of an auto-generated, unique integer,
            can’t be null and is a primary key.
        name: Represents a column of a string of 128 characters and
            can’t be null.
        cities: Rrepresents a column of an integer, can’t be null
        """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
