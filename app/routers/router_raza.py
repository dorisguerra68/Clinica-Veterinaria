from logging import exception

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db_connection import get_db
from app.controllers.raza_controller import RazaController
from app.schema_validator.raza_validator import RazaCreateValidator, RazaUpdateValidator

#creando el router
router = APIRouter()

#creamos  un adorno de una variable o función para crear la ruta de raza
@router.post("/",response_model=RazaUpdateValidator,status_code=status.HTTP_201_CREATED)
def nuevas_raza(raza_in: RazaCreateValidator, db: Session = Depends(get_db)):

    try:
        nueva_raza = RazaController.create_raza(db=db, raza_data=raza_in)
        return nueva_raza

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo añadir la raza: {str(e)}"
        )


