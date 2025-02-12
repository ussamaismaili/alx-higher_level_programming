#!/usr/bin/python3
"""list records from states table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    # database URL
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    # create engine
    engine = create_engine(db_url)

    session = Session(engine)

    # lists all State objects from the database hbtn_0e_6_usa
    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in all_states:
        print(f"{state.id}: {state.name}")

    session.close()
