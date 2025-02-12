#!/usr/bin/python3
"""list first records in states table
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    all_cities = session.query(City).order_by(City.id).all()
    for c in all_cities:
        print(f"{c.id}: {c.name} -> {c.state.name}")  # backref=state
    session.close()
