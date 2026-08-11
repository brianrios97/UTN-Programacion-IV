package com.utn.unidad_1_fundamentos.entities;

import com.utn.unidad_1_fundamentos.entities.enums.Estado;
import com.utn.unidad_1_fundamentos.entities.enums.FormaPago;
import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "pedidos")
@Data
@EqualsAndHashCode(callSuper = true)
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Pedido extends Base implements Calculable {

    private LocalDate fecha;

    @Enumerated(EnumType.STRING)
    private Estado estado;

    private Double total;

    @Enumerated(EnumType.STRING)
    private FormaPago formaPago;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "usuario_id")
    private Usuario usuario;

    @OneToMany(mappedBy = "pedido", cascade = CascadeType.ALL, orphanRemoval = true)
    @Builder.Default
    private List<DetallePedido> detalles = new ArrayList<>();

    // --- Métodos de la lógica de negocio ---

    @Override
    public void calcularTotal() {
        this.total = 0.0;
        if (detalles != null) {
            for (DetallePedido detalle : detalles) {
                detalle.calcularSubtotal();
                this.total += detalle.getSubtotal();
            }
        }
    }

    public void addDetallePedido(int cantidad, Producto producto) {
        DetallePedido detalleExistente = findDetallePedidoByProducto(producto);
        if (detalleExistente != null) {
            detalleExistente.setCantidad(detalleExistente.getCantidad() + cantidad);
        } else {
            DetallePedido nuevoDetalle = DetallePedido.builder()
                    .cantidad(cantidad)
                    .producto(producto)
                    .pedido(this)
                    .build();
            detalles.add(nuevoDetalle);
        }
        calcularTotal();
    }

    public DetallePedido findDetallePedidoByProducto(Producto producto) {
        if (detalles != null && producto != null) {
            for (DetallePedido detalle : detalles) {
                if (detalle.getProducto() != null && detalle.getProducto().getId() != null
                        && detalle.getProducto().getId().equals(producto.getId())) {
                    return detalle;
                }
            }
        }
        return null;
    }

    public void deleteDetallePedidoByProducto(Producto producto) {
        DetallePedido detalle = findDetallePedidoByProducto(producto);
        if (detalle != null) {
            detalles.remove(detalle);
            calcularTotal();
        }
    }
}