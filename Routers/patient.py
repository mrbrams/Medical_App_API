from fastapi import APIRouter
from Schemas.patient import Patients, PatientsCreate, patients
from Services.patient import PatientService


patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patient():
    data = PatientService.parse_patients(patient_data = patients)
    return {'message': 'successful', 'data': data}

@patient_router.get('/{patient_id}', status_code=200)
def get_patient_by_id(patient_id:int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'successful', 'data': data}

@patient_router.post('/', status_code=201)
def create_patient(patient: PatientsCreate):
    data = PatientService.create_patient(patient)
    return {'message': 'successful', 'data': data}

@patient_router.put('/{patient_id}', status_code=200)
def update_patient(patient_id:int, patient: PatientsCreate):
    data = PatientService.update_patient(patient_id, patient)
    return {'message': 'successful', 'data': data}

@patient_router.delete('/{patient_id}', status_code=200)
def delete_patient(patient_id:int):
    data = PatientService.delete_patient(patient_id)
    return {'message': 'successfully deleted patient', 'data': data}
