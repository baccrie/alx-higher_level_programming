#!/usr/bin/python3
"""A sequel alchemy module that performs magic"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """A module that is been mapped to db with alchemy"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
