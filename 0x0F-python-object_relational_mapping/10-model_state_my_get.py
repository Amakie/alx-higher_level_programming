#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).all()
    if state:
        for i in state:
            print("{:d}".format(i.id))
    else:
        print("Not found")
