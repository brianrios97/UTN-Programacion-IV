# Backend - API de Productos y Categorías (Unidad 6)
**Tecnicatura Universitaria en Programación a Distancia (UTN)**  
**Estudiante:** Brian Emanuel Rios

---

## 📌 Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y asíncrono para construir APIs REST.
- **SQLModel & SQLAlchemy**: ORM híbrido con Pydantic para modelado relacional y validaciones.
- **SQLite / PostgreSQL**: Persistencia en base de datos relacional.
- **CORS Middleware**: Habilitado para comunicación segura con el frontend en `http://localhost:5173`.

---

## 🏗️ Arquitectura del Backend

```text
backend/
├── app/
│   ├── core/
│   │   └── database.py          # Engine, init_db() y get_session()
│   ├── categoria/
│   │   ├── model.py             # Modelo Categoria y tabla intermedia ProductoCategoria (N:N)
│   │   ├── schema.py            # Schemas Pydantic (Create, Read, Update)
│   │   ├── service.py           # CRUD y lógica de negocio
│   │   └── router.py            # Endpoints HTTP /categorias/
│   ├── producto/
│   │   ├── model.py             # Modelo Producto con sa_column=Column(JSON) y Relationship N:N
│   │   ├── schema.py            # Schemas Pydantic con carga de relaciones
│   │   ├── service.py           # CRUD con Eager Loading (selectinload) y gestión de enlaces
│   │   └── router.py            # Endpoints HTTP /productos/ y relaciones
│   └── main.py                  # Servidor, CORS y Lifespan
├── tests/
│   └── test_api.http            # Suite de pruebas REST Client
└── requirements.txt
```

---

## 🚀 Puesta en Marcha

```bash
# 1. Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1   # En Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar servidor en modo desarrollo
fastapi dev app/main.py
```

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
- **REST Client:** Archivo ejecutable en `tests/test_api.http`.
