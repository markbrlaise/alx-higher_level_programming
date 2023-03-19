#!/usr/bin/env python3
"""

update a State object name where id is 2
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create engine
#make session with engine to interact with the db
#get State instance where id is 2
#update name then commit changes

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_update = session.query(State).filter_by(id=2).first()
    state_update.name = 'New Mexico'
    """

    well...the object is updated in the database on session.commit() 
    no need for an update method
    which doesnt exist apparently
    """
    #session.update()
    session.commit()
