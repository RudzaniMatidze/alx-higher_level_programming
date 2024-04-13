#!/usr/bin/python3
"""Starts link class to table in database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the states table

    Attributes:
    __tablename__ (str): name of the table
    id: Represents a column of a auto-generated, unique integer
        can't be null and a is primary key
    name: Represents a column of string with maximum 128 char and
        can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
