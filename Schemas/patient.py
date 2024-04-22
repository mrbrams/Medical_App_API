from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str

class PatientsCreate(BaseModel):
    name: str
    age:int
    sex: str
    weight: str
    height: str
    phone: str


patients: dict[int, Patients] = {
    0 : Patients(id=0, name="patient 0", age=25, sex="male", weight="55kg", height="160cm", phone="0801"),
    1: Patients(id=1, name="patient 1", age=29, sex="male", weight="75kg", height="176cm", phone="0802"),
    2: Patients(id=2, name="patient 2", age=33, sex="female", weight="95kg", height="192cm", phone="0803"),
    3: Patients(id=3, name="patient 3", age=37, sex="female", weight="115kg", height="208cm", phone="0804"),
}