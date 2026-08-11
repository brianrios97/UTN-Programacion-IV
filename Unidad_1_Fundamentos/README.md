# Unidad 1: Fundamentos de Spring Boot 🚀

Proyecto desarrollado para la asignatura **Programación IV** (Tecnicatura Universitaria en Programación - UTN).

## 📌 Descripción del Proyecto
Aplicación desarrollada en Spring Boot que implementa el modelo de dominio para un sistema de gestión de pedidos y productos, aplicando arquitectura por capas, mapeo objeto-relacional (JPA) y transferencia de datos mediante DTOs.

---

## 🛠️ Tecnologías Utilizadas
* **Java 21**
* **Spring Boot**
* **Spring Data JPA**
* **H2 Database** (Base de datos en memoria)
* **Lombok**
* **Maven**

---

## 🏗️ Estructura del Proyecto

* `entities/`: Modelo de dominio JPA (`Base`, `Categoria`, `Producto`, `Usuario`, `Pedido`, `DetallePedido`), interfaz `Calculable` y enumerados (`Rol`, `Estado`, `FormaPago`).
* `repositories/`: Interfaces de persistencia que extienden de `JpaRepository` (`Spring Data JPA`).
* `dtos/`: Clases de transferencia de datos organizadas por módulos (`Create`, `Edit`, `Dto`).
* `config/`: Clase `DataInitializer` para la carga e inserción inicial de datos de prueba mediante `CommandLineRunner`.

---

## 🧪 Carga de Datos y Pruebas (H2)

Al iniciar la aplicación, la clase `DataInitializer` persiste de forma automática los datos de prueba en la base de datos H2:
1. Creación e inserción de categorías (`Comidas`, `Bebidas`).
2. Creación e inserción de productos asociados.
3. Creación e inserción de un usuario de prueba.
4. Generación de un pedido con cálculo automático de totales mediante la interfaz `Calculable` y persistencia en cascada (`CascadeType.ALL`).

### 🌐 Consola Web H2
Para verificar visualmente los registros en la base de datos:
* **URL:** `http://localhost:8080/h2-console`
* **JDBC URL:** `jdbc:h2:mem:testdb`
* **User Name:** `sa`
* **Password:** *(En blanco)*