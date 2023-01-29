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
#!/usr/bin/python3
"""A module that connects to database and reads its
contents to stdout using Sql Alchemy
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
    result = session.query(State).order_by(State.id).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
