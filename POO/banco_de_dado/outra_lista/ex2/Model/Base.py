from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase

class Banco:
    def __init__(self, url):
        self.__engine = create_engine(url)

    def get_engine(self):
        return self.__engine
    
class Base(DeclarativeBase):
    pass