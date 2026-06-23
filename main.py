from fastapi import FastAPI
from  app.routers.router_home import router as router_home
from app.config.setting import Settings
app = FastAPI(
    title=settings.app_title,
    version="1.0.0",
    description=settings.app_description,
)