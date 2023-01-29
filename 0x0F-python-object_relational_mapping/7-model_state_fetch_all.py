#!/usr/bin/python3
"""
A magical model
"""


from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = 'root'
    passw = 'root'
    db = 'hbtn_0e_6_usa'
    host = 'localhost'

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passw, host, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).order_by(State.id).all()
    for obj in res:
        print('{}: {}'.format(obj.id, obj.name))
