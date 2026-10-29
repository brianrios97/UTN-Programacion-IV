import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_DB_FILE = (BASE_DIR / "database.db").as_posix()


class Settings(BaseSettings):
    # Base de datos
    DATABASE_URL: str = Field(default=f"sqlite:///{DEFAULT_DB_FILE}")

    # Clave criptogr?fica para firmar los JWT (m?nimo 32 caracteres)
    SECRET_KEY: str = Field(
        default="super-secret-key-for-jwt-signing-utn-tupad-2026-min-32-chars",
        min_length=32
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


settings = Settings()
