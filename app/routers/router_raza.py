from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db_connection import get_db

from app.schemas.raza_schema import RazaCreate, RazaUpdate, RazaResponse

# Importamos las funciones directamente del archivo del controlador
from app.controllers.raza_controller import (
    create_raza, obtener_raza, actualizar_raza, eliminar_raza
)

router = APIRouter()

@router.post("/", response_model=RazaResponse)
def crear_raza_endpoint(raza: RazaCreate, db: Session = Depends(get_db)):
    return create_raza(db, raza)

@router.get("/{id_raza}", response_model=RazaResponse)
def obtener_raza_endpoint(id_raza: int, db: Session = Depends(get_db)):
    return obtener_raza(db, id_raza)

@router.put("/{id_raza}", response_model=RazaResponse)
def actualizar_raza_endpoint(id_raza: int, raza: RazaUpdate, db: Session = Depends(get_db)):
    return actualizar_raza(db, id_raza, raza)

@router.delete("/{id_raza}")
def eliminar_raza_endpoint(id_raza: int, db: Session = Depends(get_db)):
    return eliminar_raza(db, id_raza)
