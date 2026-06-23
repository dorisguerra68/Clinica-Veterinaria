from fastapi import APIRouter

# creamos una instancia
router = APIRouter()

@router.get(path="/", tags=["Home"])
def home():
    return {"message":"Bienvenidos a Clínica Veterinaria"}