package com.youtube.jwt.controller;

import com.youtube.jwt.entity.JwtRequest;
import com.youtube.jwt.entity.JwtResponse;
import com.youtube.jwt.service.JwtService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin
public class JwtController {

    @Autowired
    private JwtService jwtService;

    @PostMapping({"/authenticate"})
    public ResponseEntity<?> createJwtToken(@RequestBody JwtRequest jwtRequest) {
        try {
            return ResponseEntity.ok(jwtService.createJwtToken(jwtRequest));
        } catch (Exception ex) {
            String msg = ex.getMessage() != null ? ex.getMessage() : "Authentication failed";
            if (msg.contains("USER_DISABLED")) {
                return ResponseEntity.status(HttpStatus.FORBIDDEN).body(java.util.Map.of("error", "user_disabled", "message", "User account is not activated"));
            } else if (msg.contains("INVALID_CREDENTIALS")) {
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(java.util.Map.of("error", "invalid_credentials", "message", "Invalid username or password"));
            }
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(java.util.Map.of("error", "authentication_error", "message", msg));
        }
    }
}
