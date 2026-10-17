# Trabajo Práctico 4 - FastAPI y Pydantic: Módulo Proveedores
**Materia:** Programación IV - Tecnicatura Universitaria en Programación (UTN)  
**Estudiante:** Brian Emanuel Rios  

---

## 📌 Descripción del Proyecto
Este proyecto extiende la API REST de gestión de catálogo (que originalmente contaba con los módulos de **Categorías** y **Productos**) incorporando el módulo completo de **Proveedores**.

Se respetó la arquitectura modular en capas:
- **`schemas.py`**: Modelos de datos con Pydantic (`ProveedorBase`, `ProveedorCreate`, `ProveedorRead`, `ProveedorUpdate`) con validaciones de longitud, obligatoriedad y tipos.
- **`services.py`**: Lógica de negocio y persistencia en memoria (listas), garantizando código único (RN-02), borrado lógico y control de estado (RN-05).
- **`routers.py`**: Endpoints REST con códigos de estado HTTP adecuados (`200`, `201`, `404`, `409`, `422`).

---

## 🚀 Instrucciones de Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Iniciar el servidor de desarrollo
```bash
fastapi dev app/main.py
```

El servidor quedará disponible en: `http://127.0.0.1:8000`

---

## 📖 Documentación Interactiva
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Pruebas (REST Client)
Dentro del directorio `tests/` se encuentra el archivo `test_api.http` con todas las peticiones listas para ejecutar (casos de éxito, paginación, filtros y todos los escenarios de error: 404, 409 y 422).
