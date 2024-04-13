#!/usr/bin/python3
"""Module that updates the name of a state in a
        MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert, update
from model_state import Base, State

if __name__ == "__main__":
    # Creates the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Creates a session factory
    Session = sessionmaker(bind=engine)

    # Creates a session object
    session = Session()

    # Retrieves the state with ID 2 from the database
    state = session.query(State).filter_by(id=2).first()

    # Updates the name of the state to "New Mexico"
    state.name = "New Mexico"

    # Commits the session to persist the changes
    session.commit()
