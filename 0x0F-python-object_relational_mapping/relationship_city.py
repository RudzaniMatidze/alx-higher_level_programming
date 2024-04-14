#!/usr/bin/python3
"""Defines the class definition of a City"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """Class City

    Attributes:
        id:  Represents a column of an auto-generated, unique integer,
            can’t be null and is a primary key.
        name: Represents a column of a string of 128 characters and
            can't be null.
        state_id: Represents a column of an integer, can’t be null
            and is a foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
