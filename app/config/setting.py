from pydantic_secttings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # son instancia
    app_title: str
    app_version: str
    app_description: str

    # construimos el objeto, donde va a procesar el objeto
   model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()