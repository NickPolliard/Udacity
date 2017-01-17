import sys

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    name = Column(String(255), nullable = False)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zipCode = Column(String(255))
    website = Column(String(255))
    id = Column(Integer, primary_key = True)

class Puppies(Base):
    __tablename__ = 'puppies'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    date_of_birth = Column(DateTime)
    gender = Column(String(255))
    weight = Column(String(255))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))

    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
