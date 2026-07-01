from datetime import date
from pydantic import BaseModel
from typing import Optional


class MascotaBase(BaseModel):
    nombre: str
    raza: str
    fecha_nacimiento: date
    peso: float
    especie: str


class MascotaCreate(MascotaBase):
    id_propietario: int
    id_raza: int


class MascotaResponse(MascotaBase):
    id_mascota: int

    class Config:
        orm_mode = True

class MascotaUpdate(MascotaBase):
    id_mascota: int
    class Config:
        orm_mode = True
