from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Food Store API - Catálogo de Productos",
    description="Backend FastAPI con SQLModel, relaciones N:N y CORS (Unidad 7 - TUPaD)",
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


@app.get("/", tags=["General"])
def read_root():
    return {
        "mensaje": "API Food Store lista (Unidad 7: Server State & Navegación)",
        "documentacion": "/docs",
    }
