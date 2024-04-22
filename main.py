from fastapi import FastAPI
from Routers.patient import patient_router
from Routers.doctor import doctor_router
from Routers.appointment import appointment_router

app = FastAPI()

app.include_router(router=patient_router, prefix="/patient", tags=["Patient"])

app.include_router(router=doctor_router, prefix="/doctor", tags=["Doctor"])
app.include_router(router=appointment_router, prefix="/appointment", tags=["Appointment"])



@app.get("/home")
def index():
    return "Welcome to AIM Hospital"
