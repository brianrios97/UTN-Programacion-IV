package com.utn.unidad_1_fundamentos.config;

import com.utn.unidad_1_fundamentos.entities.*;
import com.utn.unidad_1_fundamentos.entities.enums.*;
import com.utn.unidad_1_fundamentos.repositories.*;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;

@Configuration
public class DataInitializer {

    @Bean
    public CommandLineRunner initData(
            CategoriaRepository categoriaRepository,
            ProductoRepository productoRepository,
            UsuarioRepository usuarioRepository,
            PedidoRepository pedidoRepository
    ) {
        return args -> {
            System.out.println("==================================================");
            System.out.println("  INICIANDO CARGA DE DATOS DE PRUEBA (H2) ");
            System.out.println("==================================================");

            // 1. Crear y guardar Categorías
            Categoria catComidas = Categoria.builder()
                    .nombre("Comidas")
                    .descripcion("Platos principales y minutas")
                    .build();

            Categoria catBebidas = Categoria.builder()
                    .nombre("Bebidas")
                    .descripcion("Gaseosas y jugos fríos")
                    .build();

            categoriaRepository.save(catComidas);
            categoriaRepository.save(catBebidas);

            // 2. Crear y guardar Productos
            Producto prod1 = Producto.builder()
                    .nombre("Hamburguesa Completa")
                    .precio(8500.0)
                    .descripcion("Doble carne con queso, lechuga y tomate")
                    .stock(20)
                    .disponible(true)
                    .categoria(catComidas)
                    .build();

            Producto prod2 = Producto.builder()
                    .nombre("Gaseosa Cola 500ml")
                    .precio(2500.0)
                    .descripcion("Lata helada")
                    .stock(50)
                    .disponible(true)
                    .categoria(catBebidas)
                    .build();

            productoRepository.save(prod1);
            productoRepository.save(prod2);

            // 3. Crear y guardar Usuario
            Usuario usuario = Usuario.builder()
                    .nombre("Carlos")
                    .apellido("Pérez")
                    .mail("carlos.perez@gmail.com")
                    .celular("1122334455")
                    .contraseña("secret123")
                    .rol(Rol.USUARIO)
                    .build();

            usuarioRepository.save(usuario);

            // 4. Crear Pedido y agregar ítems mediante lógica de negocio
            Pedido pedido = Pedido.builder()
                    .fecha(LocalDate.now())
                    .estado(Estado.PENDIENTE)
                    .formaPago(FormaPago.EFECTIVO)
                    .usuario(usuario)
                    .build();

            // Probamos los métodos agregadores creados en Pedido:
            pedido.addDetallePedido(2, prod1); // 2 hamburguesas x $8500 = $17000
            pedido.addDetallePedido(1, prod2); // 1 gaseosa x $2500 = $2500

            // Guardamos el pedido (gracias a CascadeType.ALL persiste los detalles automáticamente)
            pedidoRepository.save(pedido);

            System.out.println("\n--------------------------------------------------");
            System.out.println("¡DATOS CARGADOS CON ÉXITO EN H2!");
            System.out.println("ID del Pedido creado: " + pedido.getId());
            System.out.println("Usuario del Pedido: " + pedido.getUsuario().getNombre() + " " + pedido.getUsuario().getApellido());
            System.out.println("Cantidad de ítems en el pedido: " + pedido.getDetalles().size());
            System.out.println("Total calculado automáticamente: $" + pedido.getTotal());
            System.out.println("--------------------------------------------------\n");
        };
    }
}