package com.utn.unidad_1_fundamentos.repositories;

import com.utn.unidad_1_fundamentos.entities.Pedido;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PedidoRepository extends JpaRepository<Pedido, Long> {
}