from fastapi import HTTPException
from Schemas.patient import Patients, PatientsCreate, patients

class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for patient in patient_data:
            data.append(patients[patient])
        return data
    
    @staticmethod
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient
    
    @staticmethod
    def create_patient(patient_data: PatientsCreate):
        patient_id = len(patients)
        new_patient = Patients(
            id=patient_id,
            name=patient_data.name, 
            age=patient_data.age, 
            sex=patient_data.sex, 
            weight=patient_data.weight, 
            height=patient_data.height, 
            phone=patient_data.phone)
        patients[patient_id] = new_patient
        return new_patient
    
    @staticmethod
    def update_patient(patient_id, patient_data: PatientsCreate):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        # patient.id = patient_id
        # patient.name = patient_data.name
        # patient.age = patient_data.age
        # patient.sex = patient_data.sex
        # patient.weight = patient_data.weight
        # patient.height = patient_data.height
        # patient.phone = patient_data.phone
        # return patient
        patient = Patients(
            id=patient_id,
            name=patient_data.name, 
            age=patient_data.age, 
            sex=patient_data.sex, 
            weight=patient_data.weight, 
            height=patient_data.height, 
            phone=patient_data.phone)
        patients[patient_id] = patient
        return patient
    
    @staticmethod
    def delete_patient(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        del patients[patient_id]
        return patient
