from datetime import datetime

# More cases for selection
emergency_cases = {
    "Cardiac Arrest": "Keep patient flat. Start CPR: 100-120 compressions/min. Call 911.",
    "Severe Trauma": "Apply firm pressure to wounds. Do not move the patient.",
    "Difficulty Breathing": "Sit person upright. Loosen tight clothing. Keep calm.",
    "Unconscious": "Check pulse. Place in recovery position. Call 911.",
    "Snake Bite": "Keep the limb still and below heart level. Do not cut wound."
}

non_emergency_cases = [
    "Fever & Flu", "Minor Skin Rash", "Routine Checkup", 
    "General Consultation", "Physical Therapy", "Migraine"
]

# 3 Realistically detailed hospitals
hospitals = [
    {
        "id": 1,
        "name": "City General Hospital",
        "doctor": "Dr. Sharma",
        "specialty": "Cardiologist",
        "icu_beds": 5,
        "amb_available": True,
        "phone": "911-001",
        "amb_phone": "900-111",
        "lat": "12.9716", "lng": "77.5946", # GPS
        "updated_at": datetime.now()
    },
    {
        "id": 2,
        "name": "Metro Trauma Center",
        "doctor": "Dr. Miller",
        "specialty": "Orthopedic Surgeon",
        "icu_beds": 2,
        "amb_available": True,
        "phone": "911-002",
        "amb_phone": "900-222",
        "lat": "12.9352", "lng": "77.6245",
        "updated_at": datetime.now()
    },
    {
        "id": 3,
        "name": "St. Jude Medical",
        "doctor": "Dr. Wilson",
        "specialty": "General Physician",
        "icu_beds": 8,
        "amb_available": False,
        "phone": "911-003",
        "amb_phone": "900-333",
        "lat": "12.9000", "lng": "77.5000",
        "updated_at": datetime.now()
    }
]