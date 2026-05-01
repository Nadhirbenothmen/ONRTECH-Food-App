package com.youtube.jwt.controller;

import com.youtube.jwt.entity.User;
import com.youtube.jwt.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import java.util.List;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import jakarta.annotation.PostConstruct;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostConstruct
    public void initRoleAndUser() {
        userService.initRoleAndUser();
    }

    @PostMapping("/registerNewUser")
    public ResponseEntity<?> registerNewUser(@RequestBody User user) {
        try {
            // 🧩 Vérification optionnelle : entreprise non vide
            if (user.getUserCompany() == null || user.getUserCompany().trim().isEmpty()) {
                return ResponseEntity
                        .status(HttpStatus.BAD_REQUEST)
                        .body("Le champ 'Entreprise' est obligatoire.");
            }
            // Appel du service d’enregistrement
            User savedUser = userService.registerNewUser(user);

            // ✅ Succès : on renvoie l’objet User créé avec un code 201
            return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);

        } catch (RuntimeException ex) {
            // ⚠️ Erreur fonctionnelle (ex: email déjà utilisé)
            return ResponseEntity
                    .status(HttpStatus.BAD_REQUEST)
                    .body(ex.getMessage());
        } catch (Exception ex) {
            // ⚙️ Erreur inattendue (ex: problème serveur)
            return ResponseEntity
                    .status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Une erreur interne s’est produite. Veuillez réessayer plus tard.");
        }
    }


    @PutMapping({"/activate/{userName}"})
    public User activateUser(@PathVariable String userName) {
        return userService.activateUser(userName);
    }

    @GetMapping({"/consumers"})
    public List<User> getConsumers() {
        return userService.getConsumers();
    }

    @DeleteMapping({"/deleteUser/{userName}"})
    @PreAuthorize("hasRole('Admin')")
    public String deleteUser(@PathVariable String userName) {
        userService.deleteUser(userName);
        return "User deleted: " + userName;
    }

    @GetMapping({"/forAdmin"})
    @PreAuthorize("hasRole('Admin')")
    public String forAdmin(){
        return "This URL is only accessible to the admin";
    }

    @GetMapping({"/forUser"})
    @PreAuthorize("hasRole('Consumer')")
    public String forUser(){
        return "This URL is only accessible to the user";
    }
}
