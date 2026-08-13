package com.utn.unidad_1_fundamentos.entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "detalles_pedidos")
@Data
@EqualsAndHashCode(callSuper = true)
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DetallePedido extends Base {

    private int cantidad;
    private Double subtotal;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "producto_id")
    private Producto producto;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "pedido_id")
    private Pedido pedido;

    // Método auxiliar para calcular el subtotal de este ítem
    public void calcularSubtotal() {
        if (this.producto != null && this.producto.getPrecio() != null) {
            this.subtotal = this.producto.getPrecio() * this.cantidad;
        } else {
            this.subtotal = 0.0;
        }
    }
}