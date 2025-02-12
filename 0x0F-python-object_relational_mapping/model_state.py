#!/usr/bin/python3
"""satates model"""
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
