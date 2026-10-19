from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.proveedor.routers import router as proveedor_router


# El lifespan se ejecuta al arrancar el servidor
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando base de datos...")
    init_db()  # Crea las tablas en PostgreSQL / SQLite si no existen
    print("Base de datos lista.")
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Catálogo - Unidad 5 (SQLModel)",
        description="Persistencia real en base de datos con SQLModel",
        version="1.0.0",
        lifespan=lifespan
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(proveedor_router)

    return app


app = create_app()
