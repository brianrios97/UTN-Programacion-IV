"""
Script de inicialización (seeding) de la base de datos para la Unidad 9.
Crea las tablas si no existen e inserta los usuarios iniciales (admin y user)
junto con los datos del catálogo (categorías, productos e ingredientes).
"""

from sqlmodel import Session, select
from app.core.database import engine, init_db
from app.core.security import hash_password
from app.modules.usuarios.model import Usuario
from app.categoria.model import Categoria
from app.producto.model import Producto
from app.ingrediente.model import Ingrediente


def seed():
    print("Inicializando base de datos...")
    init_db()

    with Session(engine) as session:
        # 1. Sembrar Usuarios iniciales
        admin = session.exec(select(Usuario).where(Usuario.username == "admin")).first()
        if not admin:
            admin = Usuario(
                username="admin",
                full_name="Administrador General",
                email="admin@foodstore.com",
                hashed_password=hash_password("Admin123!"),
                role="admin",
                disabled=False,
            )
            session.add(admin)
            print(" -> Usuario 'admin' creado (password: Admin123!, rol: admin)")
        else:
            print(" -> Usuario 'admin' ya existe.")

        user = session.exec(select(Usuario).where(Usuario.username == "juan")).first()
        if not user:
            user = Usuario(
                username="juan",
                full_name="Juan Perez",
                email="juan@foodstore.com",
                hashed_password=hash_password("User1234!"),
                role="user",
                disabled=False,
            )
            session.add(user)
            print(" -> Usuario 'juan' creado (password: User1234!, rol: user)")
        else:
            print(" -> Usuario 'juan' ya existe.")

        # 2. Sembrar Categorías
        categorias_data = [
            {"nombre": "Pizzas", "descripcion": "Pizzas artesanales al horno a la leña"},
            {"nombre": "Empanadas", "descripcion": "Empanadas caseras salteñas y criollas"},
            {"nombre": "Bebidas", "descripcion": "Gaseosas, aguas y cervezas bien frías"},
            {"nombre": "Postres", "descripcion": "Postres tradicionales y helados"},
        ]
        cat_map = {}
        for c_data in categorias_data:
            cat = session.exec(select(Categoria).where(Categoria.nombre == c_data["nombre"])).first()
            if not cat:
                cat = Categoria(nombre=c_data["nombre"], descripcion=c_data["descripcion"], activo=True)
                session.add(cat)
                session.commit()
                session.refresh(cat)
                print(f" -> Categoría '{cat.nombre}' creada.")
            cat_map[c_data["nombre"]] = cat

        # 3. Sembrar Ingredientes
        ingredientes_data = [
            "Queso Muzzarella",
            "Salsa de Tomate",
            "Cebolla Caramelizada",
            "Carne Cortada a Cuchillo",
            "Jamón Cocido",
            "Aceitunas Verdes",
        ]
        for ing_name in ingredientes_data:
            ing = session.exec(select(Ingrediente).where(Ingrediente.nombre == ing_name)).first()
            if not ing:
                ing = Ingrediente(nombre=ing_name, activo=True)
                session.add(ing)
                print(f" -> Ingrediente '{ing_name}' creado.")

        # 4. Sembrar Productos
        productos_data = [
            {
                "nombre": "Pizza Muzzarella Clásica",
                "descripcion": "Salsa de tomate, queso muzzarella y aceitunas verdes",
                "precio_base": 8500.0,
                "imagenes_url": ["https://images.unsplash.com/photo-1513104890138-7c749659a591"],
                "disponible": True,
                "activo": True,
                "cat_name": "Pizzas",
            },
            {
                "nombre": "Pizza Fugazzeta Rellena",
                "descripcion": "Doble masa rellena de queso con abundante cebolla",
                "precio_base": 9800.0,
                "imagenes_url": ["https://images.unsplash.com/photo-1574071318508-1cdbab80d002"],
                "disponible": True,
                "activo": True,
                "cat_name": "Pizzas",
            },
            {
                "nombre": "Empanada de Carne Criolla",
                "descripcion": "Carne suave con cebolla, huevo y condimentos tradicionales",
                "precio_base": 1200.0,
                "imagenes_url": ["https://images.unsplash.com/photo-1628294895950-9805252327bc"],
                "disponible": True,
                "activo": True,
                "cat_name": "Empanadas",
            },
            {
                "nombre": "Cerveza Quilmes Clásica 1L",
                "descripcion": "Cerveza rubia argentina clásica retornable",
                "precio_base": 3200.0,
                "imagenes_url": ["https://images.unsplash.com/photo-1608270114023-e571e2ef647b"],
                "disponible": True,
                "activo": True,
                "cat_name": "Bebidas",
            },
        ]
        for p_data in productos_data:
            cat_name = p_data.pop("cat_name")
            prod = session.exec(select(Producto).where(Producto.nombre == p_data["nombre"])).first()
            if not prod:
                prod = Producto(**p_data)
                if cat_name in cat_map:
                    prod.categorias.append(cat_map[cat_name])
                session.add(prod)
                print(f" -> Producto '{prod.nombre}' creado.")

        session.commit()
        print("\n Seeding completado exitosamente.")


if __name__ == "__main__":
    seed()
