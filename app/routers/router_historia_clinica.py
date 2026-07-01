from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_connection import get_db
from app.models.mascotas_models import Mascotas
from app.models.historias_clinicas_models import HistoriasClinicas
from app.schemas.historia_clinica_schema import (
    HistoriaClinicaCreate,
    HistoriaClinicaResponse
)

router = APIRouter(prefix="/historias", tags=["historias"])


@router.post("/", response_model=HistoriaClinicaResponse)
def crear_historia(historia: HistoriaClinicaCreate, db: Session = Depends(get_db)):
    # Validar mascota
    mascota = db.query(Mascotas).filter(
        Mascotas.id_mascota == historia.id_mascota
    ).first()
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no existe")

    # Crear
    nueva = HistoriasClinicas(**historia.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.delete("/{id_historia}")
def eliminar_historia(id_historia: int, db: Session = Depends(get_db)):
    historia = db.query(HistoriasClinicas).filter(
        HistoriasClinicas.id_historia == id_historia
    ).first()
    if not historia:
        raise HTTPException(status_code=404, detail="Historia no existe")

    db.delete(historia)
    db.commit()
    return {"mensaje": "Eliminada"}