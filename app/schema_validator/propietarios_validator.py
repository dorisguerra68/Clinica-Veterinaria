from pydantic import BaseModel, validator

class PropietarioValidator(BaseModel):
    nombre: str
    telefono: str
    direccion: str

    @validator("nombre")
    def validar_nombre(cls, v):
        if len(v) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        return v

    @validator("telefono")
    def validar_telefono(cls, v):
        if not v.isdigit():
            raise ValueError("El teléfono debe contener solo números")
        return v
