from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.mascotas_schema import MascotaCreate, MascotaResponse, MascotaUpdate
from app.controllers.mascota_controller import MascotaController

router = APIRouter(
    prefix="/mascotas",
    tags=["Mascotas"],
)

@router.post("/", response_model=MascotaResponse)
def create_mascota(data: MascotaCreate, db: Session = Depends(get_db)):
    return MascotaController.crear_mascota(db, data)

@router.get("/{id_mascota}", response_model=MascotaResponse)
def obtener_mascota(id_mascota: int, db: Session = Depends(get_db)):
    return MascotaController.obtener_mascota(db, id_mascota)

@router.put("/{id_mascota}", response_model=MascotaResponse)
def actualizar_mascota(id_mascota: int, data: MascotaUpdate, db: Session = Depends(get_db)):
    return MascotaController.actualizar_mascota(db, id_mascota, data)

@router.delete("/{id_mascota}")
def borrar_mascota(id_mascota: int, db: Session = Depends(get_db)):
    return MascotaController.borrar_mascota(db, id_mascota)
