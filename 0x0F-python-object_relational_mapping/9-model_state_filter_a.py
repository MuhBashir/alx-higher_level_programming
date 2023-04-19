#!/usr/bin/python3
"""
This script lists  State objects
that conatains letter a found from
the database `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(State.name.contains("a")).all()
    for result in results:
        print(f"{result.id}: {result.name}")
