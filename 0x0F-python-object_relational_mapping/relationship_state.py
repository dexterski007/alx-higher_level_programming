#!/usr/bin/python3
""" states class """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


meta_dat = MetaData()
Base = declarative_base(metadata=meta_dat)


class State(Base):
    """ a class for new state """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
