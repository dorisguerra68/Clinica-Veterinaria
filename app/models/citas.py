
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Citas(Base):
    __tablename__ = "citas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_mascota: Mapped[int] = mapped_column(
        ForeignKey("mascotas.id"),
        nullable=False
    )
    id_veterinario: Mapped[int] = mapped_column(
        ForeignKey("veterinarios.id"),
        nullable=False
    )
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    peso_consulta: Mapped[float] = mapped_column(Float, nullable=False)
    diagnostico: Mapped[str] = mapped_column(String(255), nullable=True)
    estado: Mapped[str] = mapped_column(String(50), nullable=False, default="programada")

    # Relaciones
    mascota: Mapped["Mascotas"] = relationship(back_populates="citas")
    veterinario: Mapped["Veterinarios"] = relationship(back_populates="citas")
    mascota_tratamientos: Mapped[list["MascotaTratamientos"]] = relationship(
        back_populates="cita",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Cita mascota_id={self.id_mascota} fecha={self.fecha}>"

