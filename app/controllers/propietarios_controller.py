from sqlalchemy.orm import Session
from app.models.propietarios_models import Propietarios
from app.schemas.propietarios_schema import PropietarioCreate, PropietarioUpdate

class PropietariosController:

    @staticmethod
    def crear_propietario(db: Session, data: PropietarioCreate):
        nuevo = Propietarios(**data.dict())
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo

    @staticmethod
    def obtener_propietarios(db: Session):
        return db.query(Propietarios).all()

    @staticmethod
    def obtener_propietario(db: Session, propietario_id: int):
        return db.query(Propietarios).filter(
            Propietarios.id_propietario == propietario_id
        ).first()

    @staticmethod
    def actualizar_propietario(db: Session, propietario_id: int, data: PropietarioUpdate):
        propietario = db.query(Propietarios).filter(
            Propietarios.id_propietario == propietario_id
        ).first()

        if not propietario:
            return None

        for key, value in data.dict(exclude_unset=True).items():
            setattr(propietario, key, value)

        db.commit()
        db.refresh(propietario)
        return propietario

    @staticmethod
    def eliminar_propietario(db: Session, propietario_id: int):
        propietario = db.query(Propietarios).filter(
            Propietarios.id_propietario == propietario_id
        ).first()

        if not propietario:
            return None

        db.delete(propietario)
        db.commit()
        return True
