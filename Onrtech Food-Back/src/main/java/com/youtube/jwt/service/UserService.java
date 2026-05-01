package com.youtube.jwt.service;

import com.youtube.jwt.dao.RoleDao;
import com.youtube.jwt.dao.UserDao;
import com.youtube.jwt.entity.Role;
import com.youtube.jwt.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.HashSet;
import java.util.Set;
import java.util.Optional;
import java.util.List;
import jakarta.mail.MessagingException;
import java.io.IOException;

@Service
public class UserService {

    @Autowired
    private UserDao userDao;

    @Autowired
    private RoleDao roleDao;

    @Autowired
    private PasswordEncoder passwordEncoder;

//    @Autowired
//    private MailService mailService;

    @Value("${app.frontend.url:http://localhost:4200/login}")
    private String frontendUrl;

    @Value("${app.support.email:support@yourapp.com}")
    private String supportEmail;

    public void initRoleAndUser() {

        Role adminRole = new Role();
        adminRole.setRoleName("Admin");
        adminRole.setRoleDescription("Admin role");
        roleDao.save(adminRole);

        Role userRole = new Role();
        userRole.setRoleName("Consumer");
        userRole.setRoleDescription("Default role for newly created record");
        roleDao.save(userRole);

        User adminUser = new User();
        adminUser.setUserName("admin123");
        adminUser.setUserPassword(getEncodedPassword("admin@pass"));
        adminUser.setUserFirstName("admin");
        adminUser.setUserLastName("admin");
        Set<Role> adminRoles = new HashSet<>();
        adminRoles.add(adminRole);
        adminUser.setRole(adminRoles);
        userDao.save(adminUser);

//        User user = new User();
//        user.setUserName("raj123");
//        user.setUserPassword(getEncodedPassword("raj@123"));
//        user.setUserFirstName("raj");
//        user.setUserLastName("sharma");
//        Set<Role> userRoles = new HashSet<>();
//        userRoles.add(userRole);
//        user.setRole(userRoles);
//        userDao.save(user);
    }

    public User registerNewUser(User user) {
        // Vérifier si l'email existe déjà
        if (userDao.existsByUserEmail(user.getUserEmail())) {
            throw new RuntimeException("❌ L'adresse e-mail est déjà utilisée. Veuillez en choisir une autre.");
        }

        // Vérifier si le username existe déjà
        if (userDao.existsByUserName(user.getUserName())) {
            throw new RuntimeException("❌ Le nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre.");
        }

        // Récupérer le rôle par défaut "Consumer"
        Optional<Role> optRole = roleDao.findById("Consumer");
        if (optRole.isEmpty()) {
            throw new RuntimeException("Role 'Consumer' not found. Init roles first.");
        }

        Role role = optRole.get();
        Set<Role> userRoles = new HashSet<>();
        userRoles.add(role);
        user.setRole(userRoles);

        // Encoder le mot de passe
        user.setUserPassword(getEncodedPassword(user.getUserPassword()));

        // ✅ Vérifier si userCompany est présent dans le JSON
        if (user.getUserCompany() == null || user.getUserCompany().isBlank()) {
            // Si le champ est vide, on le laisse null ou on peut définir une valeur par défaut
            user.setUserCompany(null); // ou "Non spécifié"
        }

        // Enregistrer le nouvel utilisateur
        return userDao.save(user);
    }


    public String getEncodedPassword(String password) {
        return passwordEncoder.encode(password);
    }

    public User activateUser(String userName) {
        Optional<User> optionalUser = userDao.findById(userName);
        if (optionalUser.isEmpty()) {
            throw new RuntimeException("User not found: " + userName);
        }
        User user = optionalUser.get();
        if (!user.isActivated()) {
            user.setActivated(true);
            userDao.save(user);
//
//            String email = user.getUserEmail();
//            if (email != null && !email.isBlank()) {
//                String actionUrl = frontendUrl.endsWith("/") ? frontendUrl + "login" : frontendUrl + "/login";
//                try {
//                    mailService.sendActivationEmail(user, actionUrl, supportEmail);
//                } catch (MessagingException | IOException ex) {
//                    System.err.println("Erreur lors de l'envoi de l'email d'activation à " + email + " : " + ex.getMessage());
//                }
//            }
        }else{
            user.setActivated(false);
            userDao.save(user);
        }
        return user;
    }

    public List<User> getUsersByRole(String roleName) {
        return userDao.findByRoleRoleName(roleName);
    }

    public List<User> getConsumers() {
        return getUsersByRole("Consumer");
    }

    public void deleteUser(String userName) {
        Optional<User> optionalUser = userDao.findById(userName);
        if (optionalUser.isEmpty()) {
            throw new RuntimeException("User not found: " + userName);
        }
        User user = optionalUser.get();
        user.getRole().clear();
        userDao.save(user);
        userDao.deleteById(userName);
    }
}
