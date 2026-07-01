from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base



class Razas(Base):
    __tablename__ = "razas"

    id_raza: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre_raza: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)

    #se relaciona con la entidad mascotas 
    mascotas: Mapped[list["Mascotas"]] = relationship(back_populates="raza")

    def __repr__(self):
       return f"<Raza {self.nombre_raza}>"


