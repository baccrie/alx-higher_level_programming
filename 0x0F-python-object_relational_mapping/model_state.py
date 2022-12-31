#!/usr/bin/python3
"""A sequel alchemy module that performs magic"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from base import Base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+mysqldb://@localhost:3306', pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)


class State(Base):
    """A module that is been mapped to db with alchemy"""
    __table_name__ = 'states'
    id = Column(integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
