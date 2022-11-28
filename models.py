from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Contact(Base):

    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(23))
