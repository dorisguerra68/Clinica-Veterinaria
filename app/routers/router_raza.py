from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_connection import get_db

from app.schemas.raza_schema import RazaCreate, RazaUpdate, RazaResponse
from app.controllers.raza_controller import (
    create_raza, obtener_raza, actualizar_raza, eliminar_raza
)

router = APIRouter()
#crear
@router.post("/", response_model=RazaResponse,status_code=201)
def crear_raza_endpoint(raza: RazaCreate, db: Session = Depends(get_db)):
    return create_raza(db, raza)

#obtener
@router.get("/{id_raza}", response_model=RazaResponse)
def obtener_raza_endpoint(id_raza: int, db: Session = Depends(get_db)):
    db_raza = obtener_raza(db, id_raza)
    if db_raza is None:
        raise HTTPException(status_code=404, detail="La raza no existe")
    return db_raza
# actualizar
@router.put("/{id_raza}", response_model=RazaResponse)
def actualizar_raza_endpoint(id_raza: int, raza: RazaUpdate, db: Session = Depends(get_db)):
    db_raza = actualizar_raza(db, id_raza, raza)
    if db_raza is None:
        raise HTTPException(status_code=404, detail="No se puede actualizar, la raza no existe")
    return db_raza
#eliminar
@router.delete("/{id_raza}", status_code=200)
def eliminar_raza_endpoint(id_raza: int, db: Session = Depends(get_db)):

    db_raza = obtener_raza(db, id_raza)
    if db_raza is None:
        raise HTTPException(status_code=404, detail="No se puede eliminar, la raza no existe")


    return eliminar_raza(db, id_raza)