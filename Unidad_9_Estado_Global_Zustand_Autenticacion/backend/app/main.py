from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.modules.usuarios.router import router as auth_router, admin_router
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router
from app.ingrediente.router import router as ingrediente_router
from app.pedidos.router import router as pedidos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Food Store API - Unidad 9 (Zustand & Autenticación JWT)",
    description=(
        "Backend seguro con autenticación JWT en cookies HttpOnly, "
        "control de acceso basado en roles (RBAC) y borrado lógico."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# Configuración de CORS con credenciales para intercambio de cookies HttpOnly (RN-03 / Consigna d)
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

# Router unificado con prefijo /api/v1
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(auth_router)
api_v1_router.include_router(admin_router)
api_v1_router.include_router(categoria_router)
api_v1_router.include_router(producto_router)
api_v1_router.include_router(ingrediente_router)
api_v1_router.include_router(pedidos_router)

app.include_router(api_v1_router)

# También incluimos los routers directamente en la raíz para compatibilidad directa
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(ingrediente_router)
app.include_router(pedidos_router)


@app.get("/", tags=["General"])
def read_root():
    return {
        "mensaje": "API Food Store lista (Unidad 9: Estado Global & Autenticación)",
        "modulos": [
            "/api/v1/auth",
            "/api/v1/admin/usuarios",
            "/api/v1/categorias",
            "/api/v1/productos",
            "/api/v1/ingredientes",
            "/api/v1/pedidos",
        ],
        "documentacion": "/docs",
    }
