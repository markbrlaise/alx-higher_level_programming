#!/usr/bin/env python3

"""

City model class with id, name and state_id as foreign key
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
