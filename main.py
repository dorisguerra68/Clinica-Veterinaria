# Esta línea creará físicamente tus tablas en pgAdmin 4 al arrancar
#Base.metadata.create_all(bind=engine)
from fastapi import FastAPI
from app.database.db_connection import engine #Base
from app.routers.router_home import router as home_router
from app.routers.router_raza import router as raza_router
from app.config.setting import settings
from sqlalchemy import text

app = FastAPI(
    title =settings.app_title,
    version =settings.app_version,
    description=settings.app_description
)

# para incluir la ruta
app.include_router(home_router)
app.include_router(raza_router, prefix="/raza", tags=["raza"])

#creamos una ruta, y haciendo una prueba
@app.get("/health-db", tags=["health"])
def db_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "La DB check ok"}