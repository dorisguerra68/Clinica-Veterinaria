from fastapi import FastAPI
from app.routers.router_home import router as home_router
from app.config.setting import settings

app = FastAPI(
    title =settings.app_title,
    version =settings.app_version,
    description=settings.app_description
)

# para incluir la ruta
app.include_router(home_router)