
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Tratamientos(Base):
    __tablename__ = "tratamientos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    dosis_por_kg: Mapped[float] = mapped_column(Float, nullable=False)
    costo: Mapped[float] = mapped_column(Float, nullable=False)

    # Forward reference: "MascotaTratamientos" es STRING
    mascota_tratamientos: Mapped[list["MascotaTratamientos"]] = relationship(
        back_populates="tratamiento",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Tratamiento {self.descripcion}>"

