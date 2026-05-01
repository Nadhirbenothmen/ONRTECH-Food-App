package com.youtube.jwt.dao;

import com.youtube.jwt.entity.User;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface UserDao extends CrudRepository<User, String> {

    List<User> findByRoleRoleName(String roleName);

    // 🔹 Vérifier si un email existe déjà
    boolean existsByUserEmail(String userEmail);

    // 🔹 Vérifier si un username existe déjà
    boolean existsByUserName(String userName);

    // 🔹 Récupérer un user par email
    Optional<User> findByUserEmail(String userEmail);

}
