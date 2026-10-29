# Backend ? FoodStore API (Unidad 8)

**Materia:** Programaci?n IV  
**Tecnicatura Universitaria en Programaci?n a Distancia ? UTN**  
**Estudiante:** Brian Emanuel Rios  

Backend desarrollado con **FastAPI** y **SQLModel**, implementando la arquitectura **Models-Schemas-Repository-UoW-Service-Router**.

---

## ??? Arquitectura Implementada
- **Repository Pattern (`app/core/repository.py`):** Encapsula el acceso a la base de datos sin ejecutar `commit()`, delegando la persistencia y permitiendo pruebas unitarias con repositorios simulados.
- **Unit of Work Pattern (`app/core/unit_of_work.py` y `app/pedidos/unit_of_work.py`):** Centraliza el control transaccional en un gestor de contexto (`with`). Si todas las operaciones tienen ?xito, ejecuta `commit()`; si ocurre cualquier excepci?n, ejecuta `rollback()` garantizando la consistencia at?mica.
- **M?dulo Pedidos (`/pedidos`):**
  - Alta at?mica de `Pedido` junto con sus `DetallePedido`.
  - Validaci?n de negocio: rechazo de lista de detalles vac?a (`422`), productos duplicados en el mismo pedido (`422`) y cantidades menores a 1 (`422`).
  - Rollback autom?tico si un producto referenciado no existe (`404`).
  - Borrado l?gico mediante `deleted_at` (`204 No Content`).
- **M?dulo Ingredientes (`/ingredientes`):** CRUD completo con validaci?n y verificaci?n de unicidad.
- **REST Client (`pedidos.http`):** Suite completa de pruebas con demostraci?n de casos exitosos y respuestas de error (`404`, `422`, `409`).
