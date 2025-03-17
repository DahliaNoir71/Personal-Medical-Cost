from sqlalchemy import Column, Integer, String, Float
from database import Base

class MedicalData(Base):
    __tablename__ = "medical_datas"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    sex = Column(String)
    bmi = Column(Float)
    children = Column(Integer)
    smoker = Column(String)
    region = Column(String)
    charges = Column(Float)
