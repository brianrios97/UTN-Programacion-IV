import os
from collections.abc import Generator
from sqlmodel import Session, SQLModel, create_engine

# 1. Configuración de la URL de conexión
# Por defecto usamos SQLite en local; si existe la variable de entorno, la toma automáticamente
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

# 2. Argumentos de conexión especiales para SQLite
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# 3. Creación del motor (engine)
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def init_db() -> None:
    """Crea todas las tablas definidas en SQLModel si aún no existen."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Provee una sesión de base de datos por cada petición HTTP y la cierra al finalizar."""
    with Session(engine) as session:
        yield session
