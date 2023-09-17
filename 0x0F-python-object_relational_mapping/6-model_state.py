#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_username, db_password, db_name), pool_pre_ping=True)
    except Exception as e:
        print(f"An error occurred while creating the engine: {str(e)}")

    Base.metadata.create_all(engine)
