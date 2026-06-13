from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#USE YOUR ACTUAL INFO
engine = create_engine('HERE')

def get_session():
    return Session(engine)