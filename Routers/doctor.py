from fastapi import APIRouter
from Schemas.doctor import Doctors, DoctorsCreate, doctors
from Services.doctor import DoctorService

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctor():
    data = DoctorService.parse_doctors(doctors_data = doctors)
    return {'message': 'successful', 'data': data}

@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id:int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/', status_code=201)
def create_doctor(doctor_data: DoctorsCreate):
    data= DoctorService.create_doctor(doctor_data)
    return {'message': 'successfully created a new doctor', 'data': data}

@doctor_router.put('/{doctor_id}', status_code=200)
def update_doctor(doctor_id:int, doctor_data: DoctorsCreate, is_available:bool):
    data = DoctorService.update_doctor(doctor_id, doctor_data, is_available)
    return {'message': 'successful', 'data': data}

@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(doctor_id:int):
    data = DoctorService.delete_doctor(doctor_id)
    return {'message': 'successfully deleted doctor', 'data': data}