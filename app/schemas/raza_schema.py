from pydantic import BaseModel, ConfigDict

class RazaBase(BaseModel):
    nombre_raza: str

class RazaCreate(RazaBase):
    pass

class RazaUpdate(RazaBase):
    pass

class RazaResponse(RazaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
