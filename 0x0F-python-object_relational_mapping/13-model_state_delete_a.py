#!/usr/bin/python3
"""Module that deletes states containing the letter
        "a" from a MySQL database using SQLAlchemy."""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    #Create the SQLAchemy engine using the provided MySQL credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    # Create engine metadata
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
