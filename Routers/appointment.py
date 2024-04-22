from fastapi import APIRouter
from Schemas.appointment import Appointments, AppointmentsCreate, appointments
from Schemas.doctor import Doctors, DoctorsCreate, doctors
from Services.appointment import AppointmentService

appointment_router = APIRouter()

@appointment_router.get('/appointment/', status_code=200)
def get_appointments():
    data = AppointmentService.parse_appointments(appointment_data=appointments)
    return {'message': 'successfully retrieved appointments', 'data': data}

@appointment_router.get('/appointment/{appointment_id}', status_code=200)
def get_appointment_by_id(appointment_id:int):
    data = AppointmentService.get_appointment_by_id(appointment_id)
    return {'message': 'successfully retrieved appointment', 'data': data}

@appointment_router.post('/appointment/', status_code=201)
def create_appointment(patient_id, appointment_data: AppointmentsCreate):
    data = AppointmentService.create_appointment(patient_id, appointment_data)
    return {'message': 'successfully created appointment', 'data': data}

@appointment_router.put('/appointment/{appointment_id}', status_code=200)
def complete_appointment(appointment_id:int):
    data = AppointmentService.complete_appointment(appointment_id)
    return {'message': 'successfully completed appointment', 'data': data}

@appointment_router.delete('/appointment/{appointment_id}', status_code=200)
def cancel_appointment(appointment_id:int):
    data = AppointmentService.cancel_appointment(appointment_id)
    return {'message': 'successfully cancelled appointment', 'data': data}

