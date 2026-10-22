from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Al iniciar el servidor creamos las tablas en la base de datos si no existen
    init_db()
    yield


app = FastAPI(
    title="API de Gestión de Productos y Categorías",
    description="Backend Full Stack con FastAPI, SQLModel y relaciones N:N (Unidad 6 - TUPaD)",
    version="1.0.0",
    lifespan=lifespan,
)

# Configuración de CORS requerida por la consigna (Página 3 del PDF)
# Permite que el frontend de React (localhost:5173) consuma la API sin bloqueos del navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de routers
app.include_router(categoria_router)
app.include_router(producto_router)


@app.get("/", tags=["General"])
def read_root():
    return {
        "mensaje": "API de Categorías y Productos lista (Unidad 6)",
        "documentacion": "/docs",
    }
