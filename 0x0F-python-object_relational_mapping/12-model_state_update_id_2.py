#!/usr/bin/python3
"""A module that connects to database and
save an instance attr to the database,
it saves the state Louisiana to the database
(This alchemy gave me nightmares before
getting to understand), but victory at last.
Vamoos!!!"""


from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_update = session.query(State).filter(State.id==2).first()
    new_update.name = 'New Mexico'
    session.add(new_update)
    session.commit()
