
from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base
#from models.propietarios_models import Propietarios
#from models.razas_models import Razas


class Mascotas(Base):
    __tablename__ = "Mascotas"

    id_mascota: Mapped[int] = mapped_column(primary_key=True, index=True)

    id_propietario: Mapped[int] = mapped_column(
        ForeignKey("propietarios.id_propietario"),
        nullable=False
    )
    id_raza: Mapped[int] = mapped_column(
        ForeignKey("razas.id_raza"),
        nullable=False
    )
    #id_historia_clinica: Mapped[int] = mapped_column(
     #   ForeignKey("historias_clinicas.id"),
      #  nullable=True
   # )
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_nacimiento: Mapped[date] = mapped_column(Date, nullable=False)
    peso: Mapped[float] = mapped_column(nullable=False)


    propietario: Mapped["Propietarios"] = relationship(
        back_populates="mascotas"
    )
    raza: Mapped["Razas"] = relationship(
        back_populates="mascotas"
    )



    #historia_clinica: Mapped["HistoriasClinicas"] = relationship(
      #  back_populates="mascota",
       # uselist=False,
        #foreign_keys=[id_historia_clinica],
        #cascade="all, delete-orphan"
    #)
    #citas: Mapped[list["Citas"]] = relationship(back_populates="mascota", cascade="all, delete-orphan")
    #mascota_tratamientos: Mapped[list["MascotaTratamientos"]] = relationship(
       # back_populates="mascota",
        #cascade="all, delete-orphan"
    #)

    def __repr__(self):
        return f"<Mascota {self.nombre}>"

