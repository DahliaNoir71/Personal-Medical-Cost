from sqlalchemy import Column, Integer, String, Float
from models.base import Base


class Insured(Base):
    __tablename__ = "insured"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)
    bmi = Column(Float, nullable=False)
    children = Column(Integer, nullable=False)
    smoker = Column(String, nullable=False)
    region = Column(String, nullable=False)
    charges = Column(Float, nullable=False)
