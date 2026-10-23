# Backend ? FoodStore API (Unidad 7)

**Materia:** Programaci?n IV  
**Tecnicatura Universitaria en Programaci?n a Distancia ? UTN**  
**Estudiante:** Brian Emanuel Rios  

Backend REST desarrollado con **FastAPI** y **SQLModel**, enfocado en la gesti?n de cat?logos y relaciones de muchos a muchos (N:N).

---

## ??? Tecnolog?as y Caracter?sticas
- **FastAPI:** Framework de alto rendimiento con validaci?n autom?tica y documentaci?n interactiva OpenAPI.
- **SQLModel:** Modelado ORM y esquemas Pydantic unificados.
- **Relaciones N:N:** `Producto` y `Categoria` asociadas a trav?s de la tabla intermedia `ProductoCategoria` con PK compuesta (`producto_id`, `categoria_id`) y atributo `es_principal` del modelo UML.
- **Validaciones:** `precio_base >= 0` mediante `Field(ge=0)`.
- **Persistencia de Colecciones:** Campo `imagenes_url` implementado con variante h?brida compatible con PostgreSQL (`ARRAY(String)`) y SQLite local (`JSON`).
- **C?digos de Estado HTTP:**
  - `POST`: `201 Created`
  - `PUT`: `200 OK`
  - `DELETE`: `204 No Content`
  - Conflictos de duplicados: `409 Conflict`
  - Entidad no encontrada: `404 Not Found`
  - Error de validaci?n: `422 Unprocessable Entity`
- **CORS Middleware:** Origen habilitado para `http://localhost:5173`.

---

## ?? Puesta en Marcha
```bash
# Crear/activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor
fastapi dev app/main.py
```
- Swagger UI: `http://localhost:8000/docs`
- Pruebas REST Client: `productos.http`
