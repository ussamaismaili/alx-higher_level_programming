#!/usr/bin/python3
"""list first records in states table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # database URL
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    # create engine
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # lists first State object from the database hbtn_0e_6_usa
    filtered_states = session.query(State).filter(
        State.name.like("%a%")
    ).order_by(State.id)

    for state in filtered_states:
        print(f"{state.id}: {state.name}")

    session.close()
