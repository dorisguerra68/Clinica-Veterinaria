from pydantic import BaseModel


class RazaBaseValidator(BaseModel):
    raza: str

# 2. Esquema para registrar datos (POST)
class RazaCreateValidator(RazaBaseValidator):
    pass

# 3. Esquema para actualizar datos (PUT).
class RazaUpdateValidator(RazaBaseValidator):
    id_raza: int

    model_config = {
        "from_attributes": True
    }
