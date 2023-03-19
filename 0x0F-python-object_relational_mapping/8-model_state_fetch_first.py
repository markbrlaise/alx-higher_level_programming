#!/usr/bin/env python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create engine the migrate tables and connect to db
#create session to db to interact with it and make queries

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    #make migrations to db
    #Base.metadata.create_all(engine)
    #create session
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = list(instance for instance in session.query(State)
            .order_by(State.id))
    print(rows[0].id, rows[0].name, sep=': ')
