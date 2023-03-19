#!/usr/bin/python3

"""

script printing all city objects in the database
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State.name, City.id, City.name)
    for instance in state.filter(State.id == City.state_id):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
