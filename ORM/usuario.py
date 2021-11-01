from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from ENV import *

engine = create_engine(CONN, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100))
    name = Column(String(50))
    password = Column(String(50))

Base.metadata.create_all(engine)
