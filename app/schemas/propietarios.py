from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base
from app.schemas.mascotas import MascotasSchema

class PropietariosSchema(Base):
    __tablename__ = "propietarios"

    id_propietario: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre_completo: Mapped[str] = mapped_column(String(150), nullable=False)
    telefono: Mapped[str] = mapped_column(String(15), nullable=False)
    direccion: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    id_mascota: Mapped[int] = mapped_column(ForeignKey("mascotas.id_mascota"), nullable=False)

    #relación de muchas mascotas a un solo propietario (inversa)
    mascotas: Mapped["list[MascotasSchema]"] = relationship(back_populates="propietarios")
