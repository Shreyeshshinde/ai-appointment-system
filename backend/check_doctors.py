# ✅ Add this block at the top of check_doctors.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Then import modules
from backend.database import SessionLocal
from backend.models import Doctor

# ✅ Actual check code
db = SessionLocal()
doctors = db.query(Doctor).all()

if not doctors:
    print("⚠️ No doctors found in the database.")
else:
    for doc in doctors:
        print(f"🩺 Name: {doc.name}, Dept: {doc.department}, Slots: {doc.available_slots}")
