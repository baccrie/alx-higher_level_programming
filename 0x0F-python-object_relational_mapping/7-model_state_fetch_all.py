#!/usr/bin/python3
"""
A magical model
"""


from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = argv[1]
    passw = argv[2]
    db = argv[3]
    host = 'localhost'

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passw, host, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).order_by(State.id)
    for obj in res:
        print('{}: {}'.format(obj.id, obj.name))
