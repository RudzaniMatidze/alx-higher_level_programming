#!/usr/bin/python3
"""Starts link class to table in database."""
import sys
from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """Class representing the states table."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_enigne('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys[3]);
            pool_pre_ping=True)
    from sqlalchemy.orm import sessionmaker
    Base.metadata.create_all(engine)
