#!/usr/bin/python3
"""A module that connects to database and
searches for a state and prints the result to stdout
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
    search = argv[4]
    count = 0

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()

    for row in result:
        if search == row.name:
            print("{}".format(row.id))
            count += 1
        else:
            pass
    if count == 0:
        print("Not found")
