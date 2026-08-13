package com.utn.unidad_1_fundamentos.repositories;

import com.utn.unidad_1_fundamentos.entities.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {

    // Método derivado requerido por la consigna (Punto 8)
    Optional<Usuario> findByMail(String mail);
}