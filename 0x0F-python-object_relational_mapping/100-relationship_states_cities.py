#!/usr/bin/python3
""" run things using sqlalchemy """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_run(username, password, db_name):
    """ run from sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()


if __name__ == '__main__':
    db_run(sys.argv[1], sys.argv[2], sys.argv[3])
