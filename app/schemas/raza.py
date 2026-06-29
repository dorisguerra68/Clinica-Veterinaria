from  sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base

#creamos una clase que nos traiga y crea una tabla con el nombre
class RazaSchema(Base):
    __tablename__ = "raza"

    id_raza: Mapped[int] = mapped_column(primary_key=True, index=True)
    raza: Mapped[str] = mapped_column(String(50), nullable=False)

    # Aquí hay una relación de 1 a muchos
    mascotas: Mapped["list[MascotasSchema]"] = relationship(back_populates="especie")