#!/usr/bin/python3
""" Defines the City class"""
from sqlalchemy import Column , Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySql database.


    Attributes:
        __tablename__ (str): name of table
        id: Represents a column of an auto_generated, unique integer,
            can't be null and is a primary key
        name: Represents a column of a string with maximum 128 char and
            can't be null
        state_id: Represents a of a ForeignKey named states.id

    """
    __tablename__ = 'cities'
    id = column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
