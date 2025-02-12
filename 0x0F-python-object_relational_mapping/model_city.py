#!/usr/bin/python3
"""satates model"""
from sqlalchemy import (Column, String, Integer, ForeignKey)
from model_state import Base


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), nullable=False)
