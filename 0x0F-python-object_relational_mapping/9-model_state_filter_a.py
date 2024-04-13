#!/usr/bin/python3
"""Module that retrieves and prints the states with
	letter a from a MySQL database using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creates the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates a session factory
    Session = sessionmaker(bind=engine)

    # Creates a session object
    session = Session()

    # Retrieves the states with letter 'a' from the
    # database and print its ID and name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
