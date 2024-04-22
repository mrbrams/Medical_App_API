from fastapi import HTTPException
from Schemas.appointment import Appointments, AppointmentsCreate, appointments
from Utilities.appointments import AppointmentHelpers
from Schemas.patient import Patients, PatientsCreate, patients
from Schemas.doctor import Doctors, DoctorsCreate, doctors
from datetime import datetime


class AppointmentService:

    @staticmethod
    def parse_appointments(appointment_data = appointments):
     data = []
     for appointment in appointment_data:
         data.append(appointment)
     return data
    
    @staticmethod
    def get_appointment_by_id(appointment_id:int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return appointment
    
    @staticmethod
    def create_appointment(patient_id: int, appointment_data: AppointmentsCreate):

    # Find the first available doctor
        available_doctor = None
        for doctor in doctors.values():
            if doctor.is_available:
                available_doctor = doctor
                break
        
        if available_doctor is None:
            raise HTTPException(status_code=404, detail="No doctors available")
    
    # Create the appointment
        appointment_id = len(appointments)
        appointment = Appointments(
        id=appointment_id,
        patient_id=patient_id,
        doctor_id=available_doctor.id,
        date=appointment_data.scheduled_datetime.strftime('%Y-%m-%d')
        )
        appointments.append(appointment)
        return appointment
    

    @staticmethod
    def complete_appointment(appointment_id: int):
    # Find the appointment to complete
        appointment = next((a for a in appointments if a.id == appointment_id), None)
        if appointment is None:
            raise HTTPException(status_code=404, detail="Appointment not found")

    # Update the appointment status and completion time
        appointment.status = 'completed'
        appointment.completed_at = datetime.now()

    # Set the doctor's availability to True
        doctor_id = appointment.doctor_id
        doctor = doctors.get(doctor_id)
        if doctor is not None:
            doctor.is_available = True
        else:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return appointment
    
    @staticmethod
    def cancel_appointment(appointment_id: int):
    # Find the appointment to cancel
        appointment = next((a for a in appointments if a.id == appointment_id), None)
        if appointment is None:
            raise HTTPException(status_code=404, detail="Appointment not found")

    # Update the appointment status to 'cancelled'
        appointment.status = 'cancelled'

    # Set the doctor's availability to True
        doctor_id = appointment.doctor_id
        doctor = doctors.get(doctor_id)
        if doctor is not None:
            doctor.is_available = True
        else:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return appointment
