#!/usr/bin/python3
""" run things using sqlalchemy """
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_run(username, password, db_name):
    """ run from sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)()
    instance = session.query(State.name, City.id, City.name).\
                             filter(State.id == City.state_id)
    for obj in instance:
        print("{}: ({}) {}".format(obj[0], obj[1], obj[2]))


if __name__ == '__main__':
    db_run(sys.argv[1], sys.argv[2], sys.argv[3])
