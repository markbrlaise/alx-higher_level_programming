#!/usr/bin/env python3

"""

import State and Base classes
create db engine
create tables if not exist from classes
create session to connect to db 
interact with db using queries through the session
"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    #connect to engine or make migartions
    Base.metadata.create_all(engine)
    #create session to interact with db
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
