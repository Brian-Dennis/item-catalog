import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    register_date = Column(String(250), nullable=False)


class Articles(Base):
    __tablename__ = 'articles'

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    create_date = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)


engine = create_engine('sqlite:///item-catalog.db')


Base.metadata.create_all(engine)