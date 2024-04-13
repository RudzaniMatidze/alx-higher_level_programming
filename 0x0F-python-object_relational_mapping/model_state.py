#!/usr/bin/python3
"""Starts link class to table in database."""

import sys
from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the states table."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
