"""Models File"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..engine import engine
#from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SimpleTextAwnser(Base):
    "DB Model for Layout File"
    __tablename__ = "layout"

    id = Column(Integer,primary_key=True)
    quest = Column(String)
    awnsr = Column(String)