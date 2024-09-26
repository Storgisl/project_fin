from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from datetime import datetime

Base = declarative_base()

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer(), primary_key=True)
    data = Column(LargeBinary, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
