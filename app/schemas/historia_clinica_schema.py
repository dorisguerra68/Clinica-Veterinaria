from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HistoriaClinicaBase(BaseModel):
    condiciones_cronicas: Optional[str] = None
    alergias: Optional[str] = None
    antecedentes_quirurgicos: Optional[str] = None
    medicamentos_actuales: Optional[str] = None

class HistoriaClinicaCreate(HistoriaClinicaBase):
    id_mascota: int

class HistoriaClinicaResponse(HistoriaClinicaBase):
    id_historia: str
    id_mascota: int
    fecha_ultima_actualizacion: datetime

    class Config:
        orm_mode = True





