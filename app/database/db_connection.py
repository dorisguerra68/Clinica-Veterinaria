# aquí creamos la connexión, declativeBase es para envocar la bd.
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config.setting import settings

# crear el motor de conexión principal
engine = create_engine(settings.database_url, echo=True)

#que es atributo autocommit es guardar la operación, y autoflush.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine

)

class Base(DeclarativeBase):
    pass

# 1º que arranque sección local
def get_db():
    db = SessionLocal() #abrimos la bd
    try:
        yield db #mantiene un estado, pausa la ejecución (llamado inyección de dependencia)
    finally:
        db.close() #aquí cerramos bd