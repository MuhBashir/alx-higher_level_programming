#!/usr/bin/python3
"""
file that contains the class definition of a State and
an instance Base = declarative_base():
"""

from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This create a class to mapped as table in the database"""

    __tablename__ = "states"

    id = Column(Integer, Sequence("state_id"), primary_key=True)
    name = Column(String(128), nullable=False)


# # for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
# #     print("{}: {}".format(state.id, state.name))
# session.close()
