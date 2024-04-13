#!/usr/bin/python3
"""
A script that creates the State "Califonia" with the City
"San Francisco" from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ = "_-main__":
    # check for correct number of args
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre-ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create  a session
    session = Session()

    # Create California state
    california = State(name="California")

    #Create San Francisco city
    san_francisco = City(name="San Francisco", state=california)

    # Add California state and San Francisco city to the session
    session.add(california)
    session.add(san_fancisco)

    # Commit changes
    session.commit()

    # #Close the session
    session.close()
