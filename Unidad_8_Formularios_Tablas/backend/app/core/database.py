import os
from pathlib import Path
from collections.abc import Generator
from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_DB_FILE = (BASE_DIR / "database.db").as_posix()
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_FILE}")

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def init_db() -> None:
    # Importamos todos los modelos para que SQLModel cree las tablas completas
    import app.categoria.model    # noqa: F401
    import app.producto.model     # noqa: F401
    import app.ingrediente.model  # noqa: F401
    import app.pedidos.models     # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
