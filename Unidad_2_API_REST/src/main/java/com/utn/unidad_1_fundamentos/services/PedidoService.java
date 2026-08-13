package com.utn.unidad_1_fundamentos.services;

import com.utn.unidad_1_fundamentos.dtos.detallepedido.DetallePedidoDto;
import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoCreate;
import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoDto;
import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoEdit;
import com.utn.unidad_1_fundamentos.entities.Pedido;
import com.utn.unidad_1_fundamentos.entities.Producto;
import com.utn.unidad_1_fundamentos.entities.Usuario;
import com.utn.unidad_1_fundamentos.entities.enums.Estado;
import com.utn.unidad_1_fundamentos.repositories.PedidoRepository;
import com.utn.unidad_1_fundamentos.repositories.ProductoRepository;
import com.utn.unidad_1_fundamentos.repositories.UsuarioRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class PedidoService {

    private final PedidoRepository pedidoRepository;
    private final UsuarioRepository usuarioRepository;
    private final ProductoRepository productoRepository;

    public PedidoService(PedidoRepository pedidoRepository, UsuarioRepository usuarioRepository, ProductoRepository productoRepository) {
        this.pedidoRepository = pedidoRepository;
        this.usuarioRepository = usuarioRepository;
        this.productoRepository = productoRepository;
    }

    public List<PedidoDto> listarTodos() {
        return pedidoRepository.findAll().stream()
                .filter(p -> !p.isEliminado())
                .map(this::toDto)
                .toList();
    }

    public PedidoDto buscarPorId(Long id) {
        Pedido p = pedidoRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Pedido no encontrado con ID: " + id));
        return toDto(p);
    }

    public PedidoDto crear(PedidoCreate dto) {
        Usuario u = usuarioRepository.findById(dto.usuarioId())
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado con ID: " + dto.usuarioId()));

        Pedido pedido = new Pedido();
        pedido.setFecha(LocalDate.now());
        pedido.setEstado(Estado.PENDIENTE);
        pedido.setFormaPago(dto.formaPago());
        pedido.setUsuario(u);
        pedido.setCreatedAt(LocalDateTime.now());
        pedido.setEliminado(false);

        // Armamos los detalles iterando la lista que vino en el JSON
        dto.detalles().forEach(detalle -> {
            Producto producto = productoRepository.findById(detalle.productoId())
                    .orElseThrow(() -> new IllegalArgumentException("Producto no encontrado con ID: " + detalle.productoId()));

            // Usamos el método que le gustó al profesor, pasándole el precio real de la BD
            pedido.addDetallePedido(detalle.cantidad(), producto);
        });

        pedido.calcularTotal();

        Pedido guardado = pedidoRepository.save(pedido);
        return toDto(guardado);
    }

    public PedidoDto actualizarEstado(Long id, PedidoEdit dto) {
        Pedido p = pedidoRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Pedido no encontrado con ID: " + id));

        p.setEstado(dto.estado());
        Pedido actualizado = pedidoRepository.save(p);
        return toDto(actualizado);
    }

    private PedidoDto toDto(Pedido p) {
        // Primero mapeamos la lista de detalles
        List<DetallePedidoDto> detallesDto = p.getDetalles().stream()
                .map(d -> new DetallePedidoDto(
                        d.getId(),
                        d.getCantidad(),
                        d.getSubtotal(),
                        d.getProducto().getNombre()
                )).toList();

        // Luego devolvemos el Pedido armado
        return new PedidoDto(
                p.getId(),
                p.getFecha(),
                p.getEstado(),
                p.getTotal(),
                p.getFormaPago(),
                p.getUsuario().getNombre() + " " + p.getUsuario().getApellido(),
                detallesDto
        );
    }
}