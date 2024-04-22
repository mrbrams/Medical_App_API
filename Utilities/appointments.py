from Schemas.appointment import Appointments, AppointmentsCreate, appointments
from Schemas.doctor import Doctors, DoctorsCreate, doctors
from fastapi import HTTPException
from Schemas.patient import Patients, PatientsCreate, patients


class AppointmentHelpers:

    @staticmethod
    def get_appointment_by_id(appointment_id:int):
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment
        return None
    
    @staticmethod
    def validate_if_doctor_is_available(appointment_data: Appointments):
        
          if appointment_data.doctor not in doctors:
            raise HTTPException(status_code=404, detail="Doctor not found")
          if appointment_data.patient not in patients:
            raise HTTPException(status_code=404, detail="Patient not found")
          for index, appointment in enumerate(appointments):
            if (
                appointment.doctor == appointment_data.doctor and
                appointment.date == appointment_data.date):
                raise HTTPException(status_code=400, detail="Appointment already exists")
        
    