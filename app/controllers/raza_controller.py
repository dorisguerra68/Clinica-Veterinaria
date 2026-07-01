from sqlalchemy.orm import Session
from app.models.razas_models import Razas
from app.schemas.raza_schema import RazaCreate, RazaUpdate


def create_raza(db: Session, raza_data: RazaCreate):
    nueva = Razas(nombre_raza=raza_data.nombre_raza)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_raza(db: Session, id_raza: int):
    return db.query(Razas).filter(Razas.id_raza == id_raza).first()

def obtener_razas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Razas).offset(skip).limit(limit).all()


def actualizar_raza(db: Session, id_raza: int, raza_data: RazaUpdate):
    raza = db.query(Razas).filter(Razas.id_raza == id_raza).first()
    if raza:
        raza.nombre_raza = raza_data.nombre_raza
        db.commit()
        db.refresh(raza)
    return raza

def eliminar_raza(db: Session, id_raza: int):
    raza = db.query(Razas).filter(Razas.id_raza == id_raza).first()
    if raza:
        db.delete(raza)
        db.commit()
    return {"mensaje": "Raza eliminada correctamente"}
