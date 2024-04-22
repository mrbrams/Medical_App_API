from pydantic import BaseModel
from Schemas.doctor import Doctors, doctors
from Schemas.patient import Patients, patients
from typing import Optional
from datetime import datetime


class Appointments(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    status:str = 'pending'
    completed_at: Optional[datetime] = None
    date: str

class AppointmentsCreate(BaseModel):
    patient_id: int
    doctor_id: int
    status:str = 'pending'
    completed_at: Optional[datetime] = None
    scheduled_datetime: datetime


appointments: list[Appointments] = []



