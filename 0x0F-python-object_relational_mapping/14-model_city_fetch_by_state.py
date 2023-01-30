#!/usr/bin/python3
"""
A magical model
"""


from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    passw = argv[2]
    db = argv[3]
    search_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    State.cities = relationship('City', order_by = City.id, back_populates = 'state')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s, c in session.query(State).filter(State.id == City.state_id).order_by(c.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name)
