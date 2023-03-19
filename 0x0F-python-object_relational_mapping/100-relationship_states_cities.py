#!/usr/bin/env python3

"""

script to create a state 'California' with 'San Francisco'
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    #create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    #create tables
    Base.metadata.create_all(engine)

    #create factory
    Session = sessionmaker(bind=engine)

    #create session
    session = Session()

    #create new state and new city objects
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    #add objects to db
    session.add(new_state, new_city)
    #commit changes to db
    session.commit()
