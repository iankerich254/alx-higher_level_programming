#!/usr/bin/python3
"""
This module defines a State class and an instance of Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the Base class
Base = declarative_base()

class State(Base):
    """
    State class that links to the 'states' table in MySQL.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
