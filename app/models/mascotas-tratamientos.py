
from datetime import date
from sqlalchemy import Date, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class MascotaTratamientos(Base):
    __tablename__ = "mascota_tratamientos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_cita: Mapped[int] = mapped_column(
        ForeignKey("citas.id"),
        nullable=False
    )
    id_tratamiento: Mapped[int] = mapped_column(
        ForeignKey("tratamientos.id"),
        nullable=False
    )
    fecha_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[date] = mapped_column(Date, nullable=True)
    dosis: Mapped[float] = mapped_column(Float, nullable=False)

    # Relaciones
    cita: Mapped["Citas"] = relationship(back_populates="mascota_tratamientos")
    tratamiento: Mapped["Tratamientos"] = relationship(back_populates="mascota_tratamientos")
    mascota: Mapped["Mascotas"] = relationship(back_populates="mascota_tratamientos")

    def __repr__(self):
        return f"<MascotaTratamiento cita_id={self.id_cita}>"
