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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).order_by(State.id).all()
    for obj in res:
        if 'a' not in obj.name:
            pass
        else:
            print('{}: {}'.format(obj.id, obj.name))
