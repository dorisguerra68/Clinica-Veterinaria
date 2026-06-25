from datetime import date as date
from sqlalchemy import  String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base
from models import especies

#creamos una clase que nos traiga y crea una tabla con el nombre
class Mascotas(Base):
    __tablename__ = "mascotas"
    id_mascota: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    raza: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_nacimiento: Mapped[date] = mapped_column(Date, nullable=False)
    id_especie: Mapped[int] = mapped_column(ForeignKey("especies.id_especie"), nullable=False)

    #relaciones inversas
    especie: Mapped["Especies"] = relationship(back_populates="mascotas")
    propietario: Mapped[list["Propietarios"]] = relationship(back_populates="mascotas")
