from datetime import date
from pydantic import BaseModel, field_validator
from typing import Optional, Any


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
        from_attributes = True


    @field_validator("raza", mode="before")
    @classmethod
    def transformar_raza_a_string(cls, v: Any) -> str:
        if hasattr(v, "nombre_raza"):
            return v.nombre_raza
        return str(v)


class MascotaUpdate(MascotaBase):
    id_mascota: int

    class Config:
        from_attributes = True
