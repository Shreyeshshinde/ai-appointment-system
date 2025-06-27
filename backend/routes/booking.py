from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from .. import schemas, models, database
from ..symptom_extractor import analyze_symptoms

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book")
def book_appointment(
    symptom: schemas.SymptomQuery = Body(...),
    db: Session = Depends(get_db)
):
    # 🔍 Analyze symptoms
    specialty = analyze_symptoms(symptom.query)
    print("🧠 Specialty returned:", specialty)  # Debug print

    # 🔎 Look up doctor by department
    doctor = db.query(models.Doctor).filter(models.Doctor.department == specialty).first()
    
    if not doctor or not doctor.available_slots:
        return {"error": f"No doctor available in department: {specialty}"}

    # 🕒 Book the first available slot
    slot = doctor.available_slots.pop(0)
    db.commit()
    
    # 💾 Create and save appointment
    appointment = models.Appointment(
        patient_name=symptom.patient_name,
        doctor_id=doctor.id,
        time=slot
    )
    db.add(appointment)
    db.commit()
    
    return {"message": f"Appointment booked with Dr. {doctor.name} at {slot}"}
