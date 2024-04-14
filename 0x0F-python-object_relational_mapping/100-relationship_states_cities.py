#!/usr/bin/python3
"""
A script that creates the State "Califonia" with the City
"San Francisco" from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ = "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre-ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create  a session
    session = Session()

    # Add California state and San Francisco city to the session
    session.add(City(name="San Francisco", state=State(name="California")))

    # Commit changes
    session.commit()
