# seed_doctors.py
# backend/seed_doctors.py
from backend.database import SessionLocal
from backend.models import Doctor



def seed_doctors():
    db = SessionLocal()

    doctors = [
        Doctor(name="Dr. John Smith", department="Cardiology", available_slots=["10:00 AM", "11:00 AM"]),
        Doctor(name="Dr. Jane Doe", department="Neurology", available_slots=["1:00 PM", "2:30 PM"]),
        Doctor(name="Dr. Emily Patel", department="Dermatology", available_slots=["9:00 AM", "4:00 PM"]),
    ]

    db.add_all(doctors)
    db.commit()
    db.close()
    print("✅ Seeded doctors successfully.")

if __name__ == "__main__":
    seed_doctors()
