from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.proveedor.routers import router as proveedor_router

# Importar los modelos para que SQLModel los registre antes de crear las tablas
import app.modules.producto.models  # noqa: F401
import app.modules.categoria.models  # noqa: F401
import app.modules.proveedor.models  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando base de datos...")
    init_db()  # Crea las tablas de Producto, Categoria y Proveedor
    print("Base de datos lista.")
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Catalogo - Unidad 5 (SQLModel)",
        description="Persistencia real en base de datos con SQLModel para los tres modulos",
        version="2.0.0",
        lifespan=lifespan,
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(proveedor_router)

    return app


app = create_app()
