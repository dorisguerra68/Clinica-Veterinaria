from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Veterinarios(Base):
    __tablename__ = "veterinarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    num_colegiado: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    especialidad: Mapped[str] = mapped_column(String(100), nullable=False)
    horario: Mapped[str] = mapped_column(String(100), nullable=True)

    # Forward reference: "Citas" es STRING
    citas: Mapped[list["Citas"]] = relationship(back_populates="veterinario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Veterinario {self.nombre}>"

