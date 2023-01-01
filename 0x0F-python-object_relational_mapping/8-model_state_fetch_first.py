#!/usr/bin/python3
"""A module that connects to database and reads only the first contents
of a table to stdout using Sql Alchemy
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
    result = session.query(State).order_by(State.id).first()

    if result = []:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
