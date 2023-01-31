#!/usr/bin/python3
"""
A magical model
"""


from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City
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

    result = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for row in result:
        print(f'{row.State.name}: ({row.City.id}) {row.City.name}')
