#!/usr/bin/python3
""" run things using sqlalchemy """
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_run(username, password, db_name, keyword):
    """ run from sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)()
    output = session.query(State).\
        filter(State.name == ((keyword,))).first()
    if output is None:
        print("Not found")
    else:
        print("{}".format(output.id))


if __name__ == '__main__':
    db_run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
