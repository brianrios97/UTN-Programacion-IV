# Trabajo Práctico Integrador — Unidad 5: SQLModel + React + Tailwind CSS
**Programación IV — Tecnicatura Universitaria en Programación a Distancia (UTN)**  
**Estudiante:** Brian Emanuel Rios

---

## 📌 Descripción General

Este proyecto integra dos partes fundamentales:
1. **Parte A (Backend):** Migración del gestor de productos a persistencia real en base de datos relacional (SQLite / PostgreSQL) utilizando **FastAPI** y **SQLModel**, conservando la arquitectura en capas (`models`, `schemas`, `services`, `routers`) y validaciones estrictas con **Pydantic**.
2. **Parte B (Frontend):** Maquetado de catálogo interactivo moderno utilizando **Vite**, **React**, **TypeScript** y **Tailwind CSS**, estructurado exclusivamente mediante componentes funcionales puros (sin hooks).

---

## 🏗️ Estructura del Repositorio

```text
Unidad_5_SQLModel_React_Tailwind/
├── backend/
│   ├── app/
│   │   ├── database.py                 # Conexión, engine y get_session()
│   │   ├── main.py                     # Lifespan init_db() y routers
│   │   └── modules/
│   │       ├── categoria/              # Módulo Categoría
│   │       ├── proveedor/              # Módulo Proveedor
│   │       └── producto/               # Módulo Producto con SQLModel
│   │           ├── models.py           # Modelos ProductoBase, Producto(table=True)
│   │           ├── schemas.py          # Schemas Pydantic Create/Read/Update
│   │           ├── services.py         # Lógica CRUD contra base de datos
│   │           └── routers.py          # Endpoints HTTP con Depends(get_session)
│   ├── tests/
│   │   └── test_api.http               # Pruebas REST Client de todos los endpoints
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── types/
    │   │   └── producto.ts             # Interface TypeScript Producto
    │   ├── components/
    │   │   ├── Navbar.tsx              # Barra superior institucional
    │   │   ├── Footer.tsx              # Pie de página
    │   │   ├── ProductoCard.tsx        # Card individual de producto
    │   │   ├── ProductoList.tsx        # Grilla responsive de productos
    │   │   └── ProductoForm.tsx        # Formulario de alta maquetado puro
    │   ├── App.tsx                     # Componente raíz con 4 productos hardcodeados
    │   └── index.css                   # Tailwind CSS v4
    ├── vite.config.ts
    └── package.json
```

---

## 🚀 Puesta en Marcha

### 1. Backend (FastAPI + SQLModel)

```bash
cd backend
python -m venv .venv
# Activar entorno (.venv\Scripts\Activate.ps1 en Windows)
pip install -r requirements.txt
fastapi dev app/main.py
```
- Documentación interactiva Swagger: `http://localhost:8000/docs`
- Pruebas REST Client en `backend/tests/test_api.http`.

### 2. Frontend (React + TypeScript + Tailwind)

```bash
cd frontend
npm install
npm run dev
```
- Servidor local en `http://localhost:5173/`.
