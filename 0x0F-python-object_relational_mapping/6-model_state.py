#!/usr/bin/python3
"""Start link class to table in database 
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
# from relationship_city import City
# from relationship_state import State

if __name__ == "__main__":
    db_URL = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine (db_URL, pool_pre_ping=True, echo=True)

    Base.metadata.create_all(engine)
