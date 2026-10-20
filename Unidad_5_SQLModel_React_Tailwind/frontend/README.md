# Frontend - Catálogo de Productos (Unidad 5)

Aplicación web desarrollada con **React 19**, **TypeScript** y **Tailwind CSS v4** sobre **Vite**, cumpliendo con los lineamientos de la **Tecnicatura Universitaria en Programación a Distancia (UTN)**.

## 🚀 Tecnologías

- **Vite 8** + **React 19**
- **TypeScript** (tipado estricto con interfaces, sin `any`)
- **Tailwind CSS v4** (`@tailwindcss/vite`)
- **Componentes Funcionales Puros** (sin `useState`, `useEffect` ni hooks de estado - HU-06 / RN-09)

## 📁 Estructura del Proyecto

```text
frontend/
├── src/
│   ├── types/
│   │   └── producto.ts         # Interface Producto (id, nombre, descripcion, precio)
│   ├── components/
│   │   ├── Navbar.tsx          # Encabezado institucional adhesivo
│   │   ├── Footer.tsx          # Pie de página informativo
│   │   ├── ProductoCard.tsx    # Tarjeta individual tipada con Producto
│   │   ├── ProductoList.tsx    # Grilla responsive que recibe Producto[]
│   │   └── ProductoForm.tsx    # Formulario de alta maquetado puro
│   ├── App.tsx                 # Componente principal que ensambla la vista
│   ├── main.tsx                # Punto de entrada de React
│   └── index.css               # Configuración global de Tailwind CSS (@import "tailwindcss";)
├── vite.config.ts              # Configuración de plugins de Vite
├── package.json
└── tsconfig.json
```

## 🛠️ Instalación y Ejecución

```bash
# 1. Instalar dependencias
npm install
# (o pnpm install)

# 2. Iniciar servidor de desarrollo
npm run dev
```

La aplicación estará disponible en `http://localhost:5173/`.

## 📦 Compilación para Producción

```bash
npm run build
```
