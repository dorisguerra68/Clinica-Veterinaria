
from datetime import datetime
from sqlalchemy import func
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base

class HistoriasClinicas(Base):
    __tablename__ = "historias_clinicas"

    id_historia: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_mascota: Mapped[int] = mapped_column(
        ForeignKey("Mascotas.id_mascota"),
        nullable=False,
        unique=True
    )
    condiciones_cronicas: Mapped[str] = mapped_column(String(255), nullable=True)
    alergias: Mapped[str] = mapped_column(String(255), nullable=True)
    antecedentes_quirurgicos: Mapped[str] = mapped_column(String(255), nullable=True)
    medicamentos_actuales: Mapped[str] = mapped_column(String(255), nullable=True)
    fecha_ultima_actualizacion: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now()
    )

    # Forward reference: "Mascotas" es STRING
    mascota: Mapped["Mascotas"] = relationship(
        back_populates="historia_clinica",
        foreign_keys=[id_mascota]
    )

    def __repr__(self):
        return f"<HistoriaClínica mascota_id={self.id_mascota}>"

