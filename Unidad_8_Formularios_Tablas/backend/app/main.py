from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router
from app.ingrediente.router import router as ingrediente_router
from app.pedidos.router import router as pedidos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Food Store API - Unidad 8 (Formularios & Tablas)",
    description="Backend con Arquitectura Repository + Unit of Work, CORS y REST Client",
    version="1.0.0",
    lifespan=lifespan,
)

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

app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(ingrediente_router)
app.include_router(pedidos_router)


@app.get("/", tags=["General"])
def read_root():
    return {
        "mensaje": "API Food Store lista (Unidad 8: Formularios & Tablas)",
        "modulos": ["/categorias", "/productos", "/ingredientes", "/pedidos"],
        "documentacion": "/docs",
    }
