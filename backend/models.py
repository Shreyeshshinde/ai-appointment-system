from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    available_slots = Column(JSON)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    doctor_id = Column(Integer)
    time = Column(String)