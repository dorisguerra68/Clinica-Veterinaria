from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.mascotas_models import Mascotas  # En plural
from app.schemas.mascotas_schema import MascotaCreate, MascotaUpdate
from app.schema_validator.mascotas_validator import MascotasValidator  # En plural

class MascotaController:

    @staticmethod
    def crear_mascota(db: Session, data: MascotaCreate):

        MascotasValidator.validar_propietario(db, data.id_propietario)
        MascotasValidator.validar_raza(db, data.id_raza)
        MascotasValidator.validar_peso(data.peso)


        nueva = Mascotas(
            nombre=data.nombre,
            especie=data.especie,
            fecha_nacimiento=data.fecha_nacimiento,
            peso=data.peso,
            id_propietario=data.id_propietario,
            id_raza=data.id_raza
        )

        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva

    @staticmethod
    def obtener_mascota(db: Session, id_mascota: int):
        # CORREGIDO: Añadida la 's' a MascotasValidator
        mascota = MascotasValidator.validar_existencia(db, id_mascota)
        return mascota

    @staticmethod
    def actualizar_mascota(db: Session, id_mascota: int, data: MascotaUpdate):

        mascota = MascotasValidator.validar_existencia(db, id_mascota)

        mascota.nombre = data.nombre
        mascota.especie = data.especie
        mascota.peso = data.peso
        mascota.fecha_nacimiento = data.fecha_nacimiento

        db.commit()
        db.refresh(mascota)
        return mascota

    @staticmethod
    def borrar_mascota(db: Session, id_mascota: int):
        mascota = MascotasValidator.validar_existencia(db, id_mascota)

        db.delete(mascota)
        db.commit()
        return {"mensaje": "Mascota borrada correctamente"}
