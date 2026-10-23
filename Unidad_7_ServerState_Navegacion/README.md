# Trabajo Pr?ctico Integrador ? Unidad 7: Server State & Navegaci?n

**Materia:** Programaci?n IV  
**Carrera:** Tecnicatura Universitaria en Programaci?n a Distancia (TUPaD) ? Universidad Tecnol?gica Nacional (UTN)  
**Estudiante:** Brian Emanuel Rios  
**Revisor:** Prof. Franco Gonz?lez  

---

## ?? Objetivo General
Desarrollar una aplicaci?n **Full Stack** conectando un frontend **React 19 + TypeScript** con un backend **FastAPI**.
- **Frontend:** Implementa el CRUD completo de Categor?as consumiendo la API REST mediante **TanStack Query** (`useQuery`, `useMutation`, invalidaci?n de cach? con `queryClient.invalidateQueries`), modal controlado con `useState` y navegaci?n multi-p?gina mediante **React Router** (`react-router-dom`).
- **Backend:** Desarrollado con **FastAPI** y **SQLModel**, implementando el paquete *Cat?logo de Productos* del diagrama UML `UML_FOOD_STORE.svg` con relaciones N:N entre `Producto` y `Categoria` a trav?s de `ProductoCategoria`, validaci?n de `precio_base >= 0`, array persistente de `imagenes_url`, respuestas `204 No Content` en eliminaci?n y archivo de pruebas `productos.http` para REST Client.

---

## ?? Estructura del Proyecto

```text
Unidad_7_ServerState_Navegacion/
??? backend/
?   ??? app/
?   ?   ??? categoria/
?   ?   ?   ??? model.py        # Modelo SQLModel Categoria
?   ?   ?   ??? router.py       # Endpoints /categorias/ (GET, POST, PUT, DELETE 204)
?   ?   ?   ??? schema.py       # Schemas Pydantic de Categoria
?   ?   ?   ??? service.py      # L?gica de negocio y consultas con selectinload
?   ?   ??? core/
?   ?   ?   ??? database.py     # Engine SQLite/PostgreSQL y sesi?n DB
?   ?   ??? producto/
?   ?   ?   ??? model.py        # Modelos Producto y tabla intermedia ProductoCategoria (N:N)
?   ?   ?   ??? router.py       # Endpoints /productos/ y vinculaci?n N:N
?   ?   ?   ??? schema.py       # Schemas Pydantic con validaci?n precio_base >= 0
?   ?   ?   ??? service.py      # L?gica de negocio de productos
?   ?   ??? main.py             # Instancia FastAPI, CORS y registro de routers
?   ??? .env                    # Configuraci?n de variables de entorno
?   ??? productos.http          # Suite completa de pruebas con REST Client
?   ??? requirements.txt        # Dependencias de Python
?   ??? README.md
?
??? frontend/
    ??? src/
    ?   ??? components/
    ?   ?   ??? Navbar.tsx         # Barra de navegaci?n con Links de React Router
    ?   ?   ??? CategoriaCard.tsx  # Tarjeta de categor?a con botones Editar y Eliminar
    ?   ?   ??? CategoriaList.tsx  # Grid de categor?as y estado vac?o
    ?   ?   ??? CategoriaModal.tsx # Modal controlado con useState para alta y edici?n
    ?   ??? pages/
    ?   ?   ??? CategoriasPage.tsx # P?gina con useQuery y useMutation de TanStack Query
    ?   ?   ??? ProductsPage.tsx   # P?gina informativa de productos y REST Client
    ?   ??? services/
    ?   ?   ??? categoria.ts       # Funciones HTTP (fetch nativo con manejo de errores)
    ?   ??? types/
    ?   ?   ??? categoria.ts       # Interface Categoria
    ?   ?   ??? producto.ts        # Interface Producto
    ?   ??? App.tsx                # Rutas /categorias y /productos con React Router
    ?   ??? main.tsx               # Proveedores QueryClientProvider y BrowserRouter
    ?   ??? index.css              # Configuraci?n de Tailwind CSS v4
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

# Iniciar servidor de desarrollo
fastapi dev app/main.py
```
- **API URL:** `http://localhost:8000`
- **Documentaci?n interactiva (Swagger UI):** `http://localhost:8000/docs`
- **Documentaci?n alternativa (ReDoc):** `http://localhost:8000/redoc`

### 2. Iniciar el Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
- **Aplicaci?n Web:** `http://localhost:5173/`

### 3. Verificar Compilaci?n de TypeScript
```bash
cd frontend
npm run build
```
Ejecuta `tsc -b && vite build` garantizando 0 errores de tipado.

---

## ?? Pruebas con REST Client
En `backend/productos.http` se incluye la suite completa de pruebas para:
1. `GET /categorias/` ? Listar categor?as.
2. `POST /categorias/` ? Crear categor?a (`201 Created`).
3. `PUT /categorias/{id}` ? Modificar categor?a (`200 OK`).
4. `DELETE /categorias/{id}` ? Eliminar categor?a (`204 No Content`).
5. `GET /productos/` ? Listar productos con categor?as asociadas.
6. `POST /productos/` ? Crear producto (`201 Created`).
7. `POST /productos/{id}/categorias/{cat_id}` ? Vincular relaci?n N:N.
8. `DELETE /productos/{id}/categorias/{cat_id}` ? Desvincular relaci?n N:N.
9. `DELETE /productos/{id}` ? Eliminar producto (`204 No Content`).
10. Validaciones de error: precios negativos (`422 Unprocessable Entity`), categor?as duplicadas (`409 Conflict`) y recursos inexistentes (`404 Not Found`).
