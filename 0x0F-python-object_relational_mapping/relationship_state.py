#!/usr/bin/env python3
"""

defining the State class inheriting from the Base declarative class
"""

from sqlalchemy import Integer, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#from relationship_city import City

Base = declarative_base(metadata=MetaData())

class State(Base):
    """

    class with id and name attributes of each state
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
