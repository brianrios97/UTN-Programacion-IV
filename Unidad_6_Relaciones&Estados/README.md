# Trabajo Práctico Integrador — Unidad 6: Relaciones y Estado
**Programación IV — Tecnicatura Universitaria en Programación a Distancia (UTN)**  
**Estudiante:** Brian Emanuel Rios

---

## 📌 Descripción General

Este proyecto Full Stack integra:
1. **Parte A (Backend):** API RESTful desarrollada con **FastAPI** y **SQLModel**, con persistencia en base de datos relacional y modelado de **relaciones Muchos a Muchos (N:N)** entre `Producto` y `Categoria` a través de la tabla intermedia `Producto_Categoria`. Configuración de **CORS** para habilitar la comunicación segura con el frontend.
2. **Parte B (Frontend):** Aplicación web interactiva desarrollada con **Vite**, **React 19**, **TypeScript** y **Tailwind CSS**. Implementa el **CRUD completo de Categorías** consumiendo la API mediante **fetch nativo**, gestionando el estado con **`useState`**, carga asincrónica con **`useEffect`**, y un **Modal interactivo** para altas y modificaciones.

---

## 🏗️ Estructura del Repositorio

```text
Unidad_6_Relaciones&Estados/
├── backend/
│   ├── app/
│   │   ├── core/database.py            # Engine, init_db() y get_session()
│   │   ├── categoria/                  # Modelos, schemas, servicios y router de Categorías
│   │   ├── producto/                   # Modelos N:N, schemas, servicios y router de Productos
│   │   └── main.py                     # Configuración de CORS y Lifespan
│   ├── tests/
│   │   └── test_api.http               # Suite de pruebas REST Client
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── types/categoria.ts          # Tipo Categoria
    │   ├── components/
    │   │   ├── Navbar.tsx              # Encabezado de la app
    │   │   ├── CategoriaCard.tsx       # Componente individual con acciones Editar/Eliminar
    │   │   ├── CategoriaList.tsx       # Grilla/tabla de categorías
    │   │   └── CategoriaModal.tsx      # Modal de alta/edición
    │   ├── App.tsx                     # Orquestador con hooks y fetch
    │   └── index.css                   # Tailwind CSS v4
    ├── vite.config.ts
    └── package.json
```

---

## 🚀 Puesta en Marcha

### 1. Iniciar el Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
fastapi dev app/main.py
```
- Swagger UI disponible en: `http://localhost:8000/docs`

### 2. Iniciar el Frontend
```bash
cd frontend
npm install
npm run dev
```
- Aplicación disponible en: `http://localhost:5173/`
