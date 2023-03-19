#!/usr/bin/env python3
"""

filter for State objects with letter a in their names
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create engine
#make session with engine to interact with the db

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(State.name == (sys.argv[4],)).order_by(State.id)
    try: 
        print(instances[0].id)
    except IndexError:
        print('Not found')