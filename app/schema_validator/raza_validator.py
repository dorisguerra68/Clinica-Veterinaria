from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.razas_models import Razas
from app.schemas.raza_schema import RazaCreate, RazaUpdate

def validar_raza_unica(db: Session, nombre_raza: str):
    raza = db.query(Razas).filter(Razas.nombre_raza == nombre_raza).first()
    if raza:
        raise HTTPException(status_code=400, detail="La raza ya existe")

def crear_raza(db: Session, raza_data: RazaCreate):
    validar_raza_unica(db, raza_data.nombre_raza)
    nueva = Razas(nombre_raza=raza_data.nombre_raza)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_raza(db: Session, id_raza: int):
    raza = db.query(Razas).filter(Razas.id_raza == id_raza).first()
    if not raza:
        raise HTTPException(status_code=404, detail="Raza no encontrada")
    return raza

def actualizar_raza(db: Session, id_raza: int, raza_data: RazaUpdate):
    raza = obtener_raza(db, id_raza)

    # sirve para que no se repita
    otra = db.query(Razas).filter(
        Razas.nombre_raza == raza_data.nombre_raza,
        Razas.id_raza != id_raza
    ).first()
    if otra:
        raise HTTPException(status_code=400, detail="Ya existe otra raza con ese nombre")

    raza.nombre_raza = raza_data.nombre_raza
    db.commit()
    db.refresh(raza)
    return raza

def eliminar_raza(db: Session, id_raza: int):
    raza = obtener_raza(db, id_raza)
    db.delete(raza)
    db.commit()
    return {"mensaje": "Raza eliminada correctamente"}
