from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):

    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    name = Column(String(56), nullable=False)
    phone = Column(String(15), nullable=True)
