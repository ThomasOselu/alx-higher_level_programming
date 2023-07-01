#!/usr/bin/python3
'''
module ORM: SQLAlchmey
link class to table in database
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() function sets up the necessary Base for mapping
Base = declarative_base()


class State(Base):
    '''State:
    class representing the states table in db;
    subclasses Base()
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
