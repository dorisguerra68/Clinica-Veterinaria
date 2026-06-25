
from sqlalchemy import  String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base

#creamos una clase que nos traiga y crea una tabla con el nombre
class Especies(Base):
    __tablename__ = "especies"

    id_especie: Mapped[int] = mapped_column(primary_key=True, index=True)
    especie: Mapped[str] = mapped_column(String(50), nullable=False)

    #aqui hay una relación de 1 a muchos
    mascotas: Mapped[list["Mascotas"]] = relationship(back_populates="especie")