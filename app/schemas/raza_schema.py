from sqlalchemy.orm import Session
from app.models.razas_models import Razas


# aquí va la logica del negocio las líneas 1 y 2

class RazaModel:
  #nos va crea bd
  @staticmethod
  def create(
          db: Session,
          raza_nombre:str
  ):
    nueva_raza = Razas(
        raza=raza_nombre

    )
    #créame está especie (categoría)
    db.add(nueva_raza)
    db.commit()
    db.refresh(nueva_raza)
    return nueva_raza