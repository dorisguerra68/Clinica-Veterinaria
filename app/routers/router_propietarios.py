from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.controllers.propietarios_controller import PropietariosController
from app.schemas.propietarios_schema import PropietarioCreate, PropietarioUpdate, PropietarioResponse

router = APIRouter(prefix="/propietarios", tags=["Propietarios"])

@router.post("/", response_model=PropietarioResponse)
def crear_propietario(data: PropietarioCreate, db: Session = Depends(get_db)):
    return PropietariosController.crear_propietario(db, data)

@router.get("/", response_model=list[PropietarioResponse])
def listar_propietarios(db: Session = Depends(get_db)):
    return PropietariosController.obtener_propietarios(db)

@router.get("/{propietario_id}", response_model=PropietarioResponse)
def obtener_propietario(propietario_id: int, db: Session = Depends(get_db)):
    propietario = PropietariosController.obtener_propietario(db, propietario_id)
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return propietario

@router.put("/{propietario_id}", response_model=PropietarioResponse)
def actualizar_propietario(propietario_id: int, data: PropietarioUpdate, db: Session = Depends(get_db)):
    propietario = PropietariosController.actualizar_propietario(db, propietario_id, data)
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return propietario

@router.delete("/{propietario_id}")
def eliminar_propietario(propietario_id: int, db: Session = Depends(get_db)):
    ok = PropietariosController.eliminar_propietario(db, propietario_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return {"message": "Propietario eliminado"}
