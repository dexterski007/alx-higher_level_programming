#!/usr/bin/python3
""" run things using sqlalchemy """
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_run(username, password, db_name):
    """ run from sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)()
    output = session.query(State).order_by(State.id).\
        filter(State.name.like('%a%'))
    for out in output:
        print("{}: {}".format(out.id, out.name))


if __name__ == '__main__':
    db_run(sys.argv[1], sys.argv[2], sys.argv[3])
