from pydantic import BaseModel

class Doctors(BaseModel):
    id:int
    name:str
    specialization:str
    phone:str
    is_available:bool = True

class DoctorsCreate(BaseModel):
    name:str
    specialization:str
    phone:str

doctors : dict[int, Doctors] = {
    0:Doctors(
        id=0,
        name="Dr. Abdul",
        specialization="Neurologist",
        phone="0901",
        is_available=True
    ),
    1:Doctors(
        id=1,
        name="Dr. Ibrahim",
        specialization="Cardiologist",
        phone="0902",
        is_available=True
    ),
    2:Doctors(
        id=2,
        name="Dr. Adam",
        specialization="Dermatologist",
        phone="0903",
        is_available=True
    ),
    3:Doctors(
        id=3,
        name="Dr. Kunle",
        specialization="Optometrist",
        phone="0904",
        is_available=True
    ),
}