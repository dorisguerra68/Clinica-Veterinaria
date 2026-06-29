from sqlalchemy.orm import Session
from app.schemas.raza_schema import RazaModel
from app.schema_validator.raza_validator import RazaCreateValidator

class RazaController:

    @staticmethod
    def create_raza(db: Session, especie_data: RazaCreateValidator):
        # Tomamos el texto limpio (.raza) que el usuario envió en el validador
        # y se lo pasamos al parámetro 'especie_nombre' que espera el modelo
        return RazaModel.create(
            db=db,
            raza_nombre=raza_data.raza
        )
