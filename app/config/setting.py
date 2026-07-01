from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_title: str
    app_version: str
    app_description: str

    #DataBase
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    #creamos el objeto que va a procesar el proyecto
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def database_url(self) -> str:
        return (f"postgresql+psycopg://{self.db_user}:{self.db_password}"
                f"@{self.db_host}:{self.db_port}/{self.db_name}")

# lA STRING QUE CONSTRUYE LA FUNCIÓN
# "postgresql://:postgresql:admin@localhost:5432/Clinica_veterinaria



settings = Settings()