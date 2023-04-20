#!/usr/bin/python3
"""
file that contains the class definition of a State and
an instance Base = declarative_base():
"""

from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State, Base


Base = declarative_base()


class City(Base):
    """This create a class to mapped as table in the database"""

    __tablename__ = "cities"

    id = Column(Integer, Sequence("state_id"), primary_key=True)
    name = Column(String(128), nullable=False)
