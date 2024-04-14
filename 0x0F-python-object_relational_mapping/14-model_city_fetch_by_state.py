#!/usr/bin/python3
"""Module that retrieves and prints a list of cities with their
        associated states from a MySQL database using SQLAlchemy.
"""

if __name__ == "__main__":

    import sys
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    # Creates the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creates a session object
    session = Session()

    # Retrieves cities and their associated states from the database
    # by joining the City and State tables based on the state_id
    # and ordering the results by city ID
    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
        # Print the city and state information
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
