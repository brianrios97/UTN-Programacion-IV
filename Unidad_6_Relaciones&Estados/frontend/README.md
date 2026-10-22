# Frontend - CRUD de Categorías (Unidad 6)
**Tecnicatura Universitaria en Programación a Distancia (UTN)**  
**Estudiante:** Brian Emanuel Rios

---

## 📌 Tecnologías Utilizadas

- **React 19** + **TypeScript** sobre **Vite**
- **Tailwind CSS v4** (`@tailwindcss/vite`)
- **Hooks de React**:
  - `useState`: Manejo del listado de categorías, estado booleano del modal y categoría en edición.
  - `useEffect`: Carga asincrónica inicial de datos al montar el componente.
- **Fetch Nativo**: Peticiones HTTP (`GET`, `POST`, `PUT`, `DELETE`) hacia la API FastAPI (`http://localhost:8000/categorias/`).

---

## 📁 Estructura del Proyecto

```text
frontend/
├── src/
│   ├── types/
│   │   └── categoria.ts         # Tipo Categoria (id, nombre, descripcion)
│   ├── components/
│   │   ├── Navbar.tsx           # Barra superior institucional
│   │   ├── CategoriaCard.tsx    # Fila/tarjeta con datos y acciones (Editar, Eliminar)
│   │   ├── CategoriaList.tsx    # Renderiza Categoria[] en tabla responsive con estado vacío
│   │   └── CategoriaModal.tsx   # Modal controlado con formulario para Alta y Edición
│   ├── App.tsx                  # Componente principal con useState, useEffect y fetch
│   ├── main.tsx                 # Montaje de React en el DOM
│   └── index.css                # Configuración de Tailwind CSS (@import "tailwindcss";)
├── vite.config.ts
└── package.json
```

---

## 🚀 Puesta en Marcha

```bash
# 1. Instalar dependencias
npm install

# 2. Iniciar en modo desarrollo
npm run dev

# 3. Compilar para producción (validación estricta de tipos)
npm run build
```

La aplicación estará disponible en **`http://localhost:5173/`**.
