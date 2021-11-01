from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = '3306'
DB = 'project_login'
USER = 'root'
PASSWORD = ''

CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

def connection():
    engine = create_engine(CONN, echo= False)
    Session = sessionmaker(bind=engine)
    return Session()