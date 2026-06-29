from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import engine

class Propietarios(Base):
    __tablename__ = "propietarios"

    id_propietario: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
    direccion: Mapped[str] = mapped_column(String(255), nullable=False)

    # Forward reference: "Mascotas" es STRING para evitar import circular
    mascotas: Mapped[list["Mascotas"]] = relationship(
        back_populates="propietario",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Propietario {self.nombre}>"

