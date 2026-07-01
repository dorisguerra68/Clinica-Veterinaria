from fastapi import HTTPException, FastAPI
from sqlalchemy.orm import Session
from starlette import status

from app.models.mascotas_models import Mascotas
from app.models.propietarios_models import Propietarios
from app.models.razas_models import Razas

class MascotasValidator:

    @staticmethod
    def validar_existencia(db: Session, id_mascota: int) -> Mascotas:
        mascota= db.query(Mascotas).filter(Mascotas.id_mascota == id_mascota).first()
        if not mascota:
            raise HTTPException(status_code=404, detail="Mascota no existe o no encontrado")
        return mascota

    @staticmethod
    def validar_propietario(db: Session, id_propietario: int):
        propietario= db.query(Propietarios.id_propietario== id_propietario).first()
        if not propietario:
            raise HTTPException(status_code=404, detail="Propietario no encontrado")
        return propietario

    @staticmethod
    def validar_raza(db: Session, id_raza: int):
        raza = db.query(Razas.id_raza== id_raza).first()
        if not raza:
            raise HTTPException(status_code=404, detail="Raza no encontrado")
        return raza

    @staticmethod
    def validar_peso(peso: int):

        if peso <= 0:
            raise HTTPException(status_code=400, detail="Peso no valido")

        if peso >= 100:
            raise HTTPException(status_code=400, detail="Peso muy alto para una mascota")

        return peso