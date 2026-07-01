from fastapi import FastAPI
from sqlalchemy import text
from app.config.setting import settings


from app.database.db_connection import engine, Base
from app.models.razas_models import Razas
from app.models.mascotas_models import Mascotas
from app.models.propietarios_models import Propietarios


Base.metadata.create_all(bind=engine)

#  se importa al routers
from app.routers.router_home import router as home_router
from app.routers.router_raza import router as raza_router
from app.routers.router_propietarios import router as propietarios_router
from app.routers.router_mascota import router as mascota_router

# configurar FASTAPI
app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    description=settings.app_description
)

# rutas
app.include_router(home_router)
app.include_router(raza_router, prefix="/razas", tags=["Razas"])
app.include_router(propietarios_router)
app.include_router(mascota_router)

# 6. enpoint de ejemplo
@app.get("/health-db", tags=["health"])
def db_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "La DB check ok"}
