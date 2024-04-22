from fastapi import HTTPException
from Schemas.doctor import Doctors, DoctorsCreate, doctors

class DoctorService:

    @staticmethod
    def parse_doctors(doctors_data = doctors):
        data = []
        for doctor in doctors_data:
            data.append(doctors[doctor])
        return data
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(status_code= 400, detail='doctor not found')
        return doctor
    
    @staticmethod
    def create_doctor(doctor_data: DoctorsCreate):
        doctor_id = len(doctors)
        new_doctor = Doctors(
            id = doctor_id,
            name = doctor_data.name,
            specialization= doctor_data.specialization,
            phone= doctor_data.phone,)
        doctors[doctor_id] = new_doctor
        return new_doctor
    
    @staticmethod
    def update_doctor(doctor_id, doctor_data: DoctorsCreate, is_available: bool):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor = Doctors(
            id = doctor_id,
            name = doctor_data.name,
            specialization = doctor_data.specialization,
            phone = doctor_data.phone)
        doctors[doctor_id] = doctor
        # Update the doctor's availability
        doctor.is_available = is_available
        return doctor
    
    @staticmethod
    def delete_doctor(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(status_code=400, detail="Could not find doctor")
        del doctors[doctor_id]
        return doctor

