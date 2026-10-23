# Trabajo Pr?ctico Integrador ? Unidad 8: Formularios & Tablas

**Materia:** Programaci?n IV  
**Carrera:** Tecnicatura Universitaria en Programaci?n a Distancia (TUPaD) ? Universidad Tecnol?gica Nacional (UTN)  
**Estudiante:** Brian Emanuel Rios  
**Revisor:** Prof. Franco Gonz?lez  

---

## ?? Objetivo General
Desarrollar una aplicaci?n **Full Stack** conectando un frontend **React 19 + TypeScript** con un backend **FastAPI**.
- **Frontend:** Implementa los CRUD completos de **Categor?as**, **Productos** e **Ingredientes** utilizando **TanStack Query** (`useQuery`, `useMutation`), **TanStack Form** (`useForm`, `form.Field` con validaci?n tipada por campo y por evento) y **TanStack Table v8** (`useReactTable`, ordenamiento con `getSortedRowModel`, paginaci?n con `getPaginationRowModel`), modals controlados con `useState` y navegaci?n multi-p?gina mediante **React Router** (`react-router-dom`).
- **Backend:** Desarrollado con **FastAPI** y **SQLModel**, implementa la arquitectura en capas **Models-Schemas-Repository-UoW-Service-Router**:
  - Base Repository gen?rico (`BaseRepository[ModelType]`) y Base Unit of Work (`AbstractUnitOfWork`).
  - M?dulo **Pedidos** y **DetallePedido**: creaci?n at?mica transaccional con c?lculo autom?tico de totales y validaciones de negocio (detalles no vac?os, productos no repetidos, referencias existentes).
  - Eliminaci?n l?gica (*soft delete*) con `deleted_at`.
  - M?dulos de **Categor?a**, **Producto** e **Ingrediente**.
  - Suite de pruebas de integraci?n con REST Client en `pedidos.http`.

---

## ?? Estructura del Proyecto

```text
Unidad_8_Formularios_Tablas/
??? backend/
?   ??? app/
?   ?   ??? core/
?   ?   ?   ??? database.py        # Configuraci?n del engine y sesi?n
?   ?   ?   ??? repository.py      # Repositorio base gen?rico BaseRepository
?   ?   ?   ??? unit_of_work.py    # Unit of Work base AbstractUnitOfWork
?   ?   ??? categoria/             # CRUD de Categor?as
?   ?   ??? producto/              # CRUD de Productos y tabla intermedia N:N
?   ?   ??? ingrediente/           # CRUD de Ingredientes
?   ?   ??? pedidos/               # M?dulo Pedidos con UoW y Repository
?   ?   ?   ??? models.py          # Modelos Pedido y DetallePedido
?   ?   ?   ??? repository.py      # PedidoRepository, DetallePedidoRepository
?   ?   ?   ??? schemas.py         # Schemas y validadores de negocio
?   ?   ?   ??? service.py         # PedidoService con atomicidad
?   ?   ?   ??? unit_of_work.py    # PedidosUnitOfWork
?   ?   ?   ??? router.py          # Endpoints /pedidos (201, 200, 204, 404, 422)
?   ?   ??? main.py                # Instancia FastAPI, CORS y registro de routers
?   ??? pedidos.http               # Suite completa de pruebas con REST Client
?   ??? requirements.txt           # Dependencias de Python
?   ??? seed.py                    # Script de precarga de datos de prueba
?   ??? README.md
?
??? frontend/
    ??? src/
    ?   ??? components/
    ?   ?   ??? Navbar.tsx            # Barra de navegaci?n con Links de React Router
    ?   ?   ??? TablePagination.tsx   # Controles reutilizables de paginaci?n para TanStack Table
    ?   ?   ??? CategoriaModal.tsx    # Modal con TanStack Form para Categor?as
    ?   ?   ??? ProductoModal.tsx     # Modal con TanStack Form para Productos
    ?   ?   ??? IngredienteModal.tsx  # Modal con TanStack Form para Ingredientes
    ?   ??? pages/
    ?   ?   ??? CategoriasPage.tsx    # CRUD de Categor?as con TanStack Table v8
    ?   ?   ??? ProductsPage.tsx      # CRUD de Productos con TanStack Table v8
    ?   ?   ??? IngredientesPage.tsx  # CRUD de Ingredientes con TanStack Table v8
    ?   ??? services/
    ?   ?   ??? categoria.ts          # Servicios API Categor?as
    ?   ?   ??? producto.ts           # Servicios API Productos
    ?   ?   ??? ingrediente.ts        # Servicios API Ingredientes
    ?   ??? types/
    ?   ?   ??? categoria.ts          # Interface Categoria
    ?   ?   ??? producto.ts           # Interface Producto
    ?   ?   ??? ingrediente.ts        # Interface Ingrediente
    ?   ??? App.tsx                   # Rutas sin l?gica de negocio
    ?   ??? main.tsx                  # QueryClientProvider y BrowserRouter
    ?   ??? index.css                 # Tailwind CSS v4
    ??? package.json
    ??? README.md
```

---

## ?? Gu?a de Ejecuci?n

### 1. Iniciar el Backend (FastAPI)
```bash
cd backend
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1   # En Windows PowerShell
# o bien: source .venv/bin/activate

# Opcional: Cargar datos iniciales de prueba
python seed.py

# Iniciar servidor de desarrollo
fastapi dev app/main.py
```
- **API URL:** `http://localhost:8000`
- **Documentaci?n Swagger UI:** `http://localhost:8000/docs`

### 2. Iniciar el Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
- **Aplicaci?n Web:** `http://localhost:5173/`

### 3. Validar Compilaci?n TypeScript
```bash
cd frontend
npm run build
```
Ejecuta `tsc -b && vite build` garantizando 0 errores.
