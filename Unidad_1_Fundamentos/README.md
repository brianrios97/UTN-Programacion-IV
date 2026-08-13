# Unidad 1: Fundamentos de Spring Boot y Persistencia JPA 🚀

**Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional (UTN)**  
**Cátedra:** Programación IV  
**Repositorio Oficial:** [https://github.com/brianrios97/UTN-Programacion-IV](https://github.com/brianrios97/UTN-Programacion-IV)  

---

## 📌 Descripción del Proyecto
Aplicación desarrollada en **Spring Boot** que implementa el modelo de dominio para un sistema de gestión de pedidos y productos, aplicando arquitectura por capas, mapeo objeto-relacional (JPA), persistencia de datos en memoria (H2) y transferencia de información mediante DTOs.

---

## 🛠️ Tecnologías Utilizadas
* **Java 21 / 24**
* **Spring Boot 3.2.5**
* **Spring Data JPA / Hibernate**
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

---

## 🌐 Consola Web H2
Para verificar visualmente las tablas y los registros en la base de datos:
* **URL:** [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
* **JDBC URL:** `jdbc:h2:mem:testdb`
* **User Name:** `sa`
* **Password:** *(En blanco)*

---

## 🚀 Instrucciones de Ejecución

### Clonar repositorio:
```bash
git clone https://github.com/brianrios97/UTN-Programacion-IV.git
cd UTN-Programacion-IV/Unidad_1_Fundamentos
```

### Ejecutar con Maven Wrapper:
```bash
./mvnw spring-boot:run
```
o en Windows:
```powershell
.\mvnw.cmd spring-boot:run
```