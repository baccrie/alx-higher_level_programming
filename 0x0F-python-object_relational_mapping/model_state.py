#!/usr/bin/python3

"""
The Magical SqlAlchemy has started
"""

from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


user = 'root'
passw = 'root'
db = 'hbtn_0e_6_usa'
host = 'localhost'

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                       .format(user, passw, host, db), pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    """A state class that inherits from the alchemy base"""
    __tablename__ = 'states'
    id = Column(nullable=false, primary_key=True, unique=True)
    name = Column(String(128), null=false)


Base.metadata.create_all(engine)
