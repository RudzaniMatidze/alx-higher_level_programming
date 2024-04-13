#!/usr/bin/python3
""" Defines the City class"""
from sqlalchemey import Column , Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents acity for a MySql database.

    """
    __tablename__ = 'cities'
    id = column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
