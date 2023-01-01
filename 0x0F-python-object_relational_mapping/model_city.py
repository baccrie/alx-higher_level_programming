#!/usr/bin/python3
"""A sequel alchemy module that performs magic"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKeys
from model_state import State, Base

Base = declarative_base()


class City(Base):
    """A module that is been mapped to db with alchemy"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKeys('states.id'))
