from datetime import datetime, timezone
from sqlmodel import Session, SQLModel
from app.core.database import engine, init_db
from app.categoria.model import Categoria
from app.producto.model import Producto
from app.ingrediente.model import Ingrediente
from app.pedidos.models import Pedido, DetallePedido

def seed():
    # Reiniciar tablas limpias
    SQLModel.metadata.drop_all(engine)
    init_db()

    with Session(engine) as session:
        # 1. Categorias
        cat_pizzas = Categoria(nombre="Pizzas", descripcion="Pizzas artesanales con masa madre al horno de barro")
        cat_burgers = Categoria(nombre="Hamburguesas", descripcion="Hamburguesas gourmet con blend especial y pan brioche")
        cat_bebidas = Categoria(nombre="Bebidas", descripcion="Bebidas frias, aguas y cervezas artesanales")
        cat_postres = Categoria(nombre="Postres", descripcion="Postres caseros, helados y dulces del dia")
        session.add_all([cat_pizzas, cat_burgers, cat_bebidas, cat_postres])
        session.commit()
        session.refresh(cat_pizzas)
        session.refresh(cat_burgers)
        session.refresh(cat_bebidas)
        session.refresh(cat_postres)

        # 2. Ingredientes
        ing_mozza = Ingrediente(nombre="Mozzarella Fior di Latte")
        ing_tomate = Ingrediente(nombre="Salsa de Tomate San Marzano")
        ing_albahaca = Ingrediente(nombre="Albahaca Fresca")
        ing_cheddar = Ingrediente(nombre="Queso Cheddar Fundido")
        ing_panceta = Ingrediente(nombre="Panceta Ahumada Crocante")
        ing_carne = Ingrediente(nombre="Medallon Blend de Ojo de Bife")
        session.add_all([ing_mozza, ing_tomate, ing_albahaca, ing_cheddar, ing_panceta, ing_carne])
        session.commit()

        # 3. Productos
        prod_marga = Producto(
            nombre="Pizza Margherita Clasica",
            descripcion="Salsa de tomate, mozzarella fior di latte, albahaca y aceite de oliva virgen extra",
            precio_base=8500.0,
            imagenes_url=["https://images.unsplash.com/photo-1513104890138-7c749659a591"],
            disponible=True,
            categorias=[cat_pizzas]
        )
        prod_4quesos = Producto(
            nombre="Pizza Cuatro Quesos",
            descripcion="Mozzarella, gorgonzola, provolone y reggianito",
            precio_base=9800.0,
            imagenes_url=["https://images.unsplash.com/photo-1574071318508-1cdbab80d002"],
            disponible=True,
            categorias=[cat_pizzas]
        )
        prod_burger_bacon = Producto(
            nombre="Burger Bacon Doble Cheddar",
            descripcion="Doble medallon de 120g, queso cheddar fundido, panceta crocante y salsa barbacoa",
            precio_base=11200.0,
            imagenes_url=["https://images.unsplash.com/photo-1568901346375-23c9450c58cd"],
            disponible=True,
            categorias=[cat_burgers]
        )
        session.add_all([prod_marga, prod_4quesos, prod_burger_bacon])
        session.commit()
        session.refresh(prod_marga)
        session.refresh(prod_4quesos)
        session.refresh(prod_burger_bacon)

        # 4. Pedidos con DetallePedido (Demostracion UoW)
        ped1 = Pedido(fecha=datetime.now(timezone.utc), estado="PENDIENTE", total=26800.0)
        session.add(ped1)
        session.flush()

        det1_1 = DetallePedido(pedido_id=ped1.id, producto_id=prod_marga.id, cantidad=2, precio_unitario=8500.0)
        det1_2 = DetallePedido(pedido_id=ped1.id, producto_id=prod_4quesos.id, cantidad=1, precio_unitario=9800.0)
        session.add_all([det1_1, det1_2])

        ped2 = Pedido(fecha=datetime.now(timezone.utc), estado="CONFIRMADO", total=11200.0)
        session.add(ped2)
        session.flush()
        det2_1 = DetallePedido(pedido_id=ped2.id, producto_id=prod_burger_bacon.id, cantidad=1, precio_unitario=11200.0)
        session.add(det2_1)

        session.commit()

    print("Seed data successfully inserted into database.db!")

if __name__ == "__main__":
    seed()
