//package com.youtube.jwt.service;
//
//import com.youtube.jwt.entity.User;
//import jakarta.mail.MessagingException;
//import jakarta.mail.internet.MimeMessage;
//import org.springframework.mail.SimpleMailMessage;
//import org.springframework.mail.javamail.JavaMailSender;
//import org.springframework.mail.javamail.MimeMessageHelper;
//import org.springframework.stereotype.Service;
//import org.springframework.core.io.ClassPathResource;
//import org.springframework.core.io.Resource;
//
//import java.io.IOException;
//import java.nio.charset.StandardCharsets;
//import java.time.Year;
//import java.util.Optional;
//
//@Service
//public class MailService {
//    private final JavaMailSender mailSender;
//
//    public MailService(JavaMailSender mailSender) {
//        this.mailSender = mailSender;
//    }
//
//    public void sendSimpleMessage(String to, String subject, String text) {
//        SimpleMailMessage message = new SimpleMailMessage();
//        message.setTo(to);
//        message.setSubject(subject);
//        message.setText(text);
//        mailSender.send(message);
//    }
//
//    public void sendHtmlMessage(String to, String subject, String htmlBody) throws MessagingException {
//        MimeMessage mimeMessage = mailSender.createMimeMessage();
//        MimeMessageHelper helper = new MimeMessageHelper(mimeMessage, "utf-8");
//        helper.setTo(to);
//        helper.setSubject(subject);
//        helper.setText(htmlBody, true);
//        mailSender.send(mimeMessage);
//    }
//
//    public void sendActivationEmail(User user, String actionUrl, String supportEmail) throws MessagingException, IOException {
//        if (user == null || user.getUserEmail() == null || user.getUserEmail().isBlank()) {
//            throw new IllegalArgumentException("User ou email invalide pour envoi d'activation");
//        }
//
//        Resource resource = new ClassPathResource("templates/activation-email.html");
//        String template;
//        try (var is = resource.getInputStream()) {
//            template = new String(is.readAllBytes(), StandardCharsets.UTF_8);
//        }
//
//        String firstName = Optional.ofNullable(user.getUserFirstName()).orElse("");
//        String userName = Optional.ofNullable(user.getUserName()).orElse("");
//        String email = Optional.ofNullable(user.getUserEmail()).orElse("");
//        String year = String.valueOf(Year.now().getValue());
//
//        String body = template
//                .replace("{{firstName}}", escapeHtml(firstName))
//                .replace("{{userName}}", escapeHtml(userName))
//                .replace("{{email}}", escapeHtml(email))
//                .replace("{{action_url}}", escapeHtml(actionUrl == null ? "" : actionUrl))
//                .replace("{{support_email}}", escapeHtml(supportEmail == null ? "" : supportEmail))
//                .replace("{{year}}", year);
//
//        sendHtmlMessage(user.getUserEmail(), "Votre compte a été activé", body);
//    }
//
//    private String escapeHtml(String s) {
//        if (s == null) return "";
//        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;");
//    }
//}
