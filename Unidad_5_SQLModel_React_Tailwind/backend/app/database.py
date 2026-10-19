import os
from sqlmodel import SQLModel, create_engine, Session
from typing import Generator

# Si hay variable de entorno usa PostgreSQL, sino crea una base local SQLite
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///database.db"
)

# SQLite necesita este argumento extra para manejar múltiples hilos de FastAPI
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

# 1. El motor de base de datos
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


# 2. Función para crear las tablas al iniciar la app
def init_db():
    SQLModel.metadata.create_all(engine)


# 3. Dependencia para inyectar la sesión en cada endpoint
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
