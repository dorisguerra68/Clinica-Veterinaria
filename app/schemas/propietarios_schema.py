from pydantic import BaseModel
from typing import Optional


class PropietarioBase(BaseModel):
    nombre: str
    telefono: str
    direccion: str

class PropietarioCreate(PropietarioBase):
    pass

class PropietarioUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class PropietarioResponse(PropietarioBase):
    id_propietario: int

    class Config:
        orm_mode = True
