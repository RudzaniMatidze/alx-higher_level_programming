#!/usr/bin/python3
""" Module that defines the City class using SQLAlchemy """

from sqlalchemy import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class City(Base):
    """Represents a City for a MySQL database.

    Attributes:
        __tablename__ (str): name of the table
        id: Represents a column of an auto-generated, unique integer,
            can't be null and is a primary key
        name: Represents a column of a string with maximum 128 characters
            and can'tbe null
        state.id: Represents a column of string id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state.id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
