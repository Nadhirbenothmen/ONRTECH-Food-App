import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { UserService } from '../_Services/user.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register-consumer',
  templateUrl: './register-consumer.component.html',
  styleUrls: ['./register-consumer.component.css']
})
export class RegisterConsumerComponent implements OnInit {

  showPassword: boolean = false;
  showConfirmPassword: boolean = false;

  constructor(
    private userService: UserService,
    private router: Router,
    private toastr: ToastrService
  ) { }

  ngOnInit(): void {
  }

  togglePasswordVisibility() {
    this.showPassword = !this.showPassword;
  }

  toggleConfirmPasswordVisibility() {
    this.showConfirmPassword = !this.showConfirmPassword;
  }

  register(registerForm: NgForm) {
    // Vérifier si les mots de passe correspondent
    if (registerForm.value.userPassword !== registerForm.value.confirmPassword) {
      this.toastr.error(
        'Passwords do not match. Please try again.',
        'Password Error',
        {
          timeOut: 5000,
          progressBar: true,
          closeButton: true
        }
      );
      return;
    }

    this.userService.registerNewUser(registerForm.value).subscribe(
      (res: any) => {
        console.log('User registered successfully:', res);
        this.toastr.success(
          'Your account has been created! Once the admin activates your account you will be able to log in.',
          'Registration Successful',
          {
            timeOut: 6000,
            progressBar: true,
            closeButton: true
          }
        );
        registerForm.reset();
        setTimeout(() => {
          this.router.navigate(['/login']);
        }, 2000);
      },
      err => {
        console.error('=== ERROR DETAILS ===');
        console.error('Full error object:', err);
        console.error('Error status:', err.status);
        console.error('Error error:', err.error);
        console.error('Error message:', err.message);
        console.error('====================');
        
        // Convertir toute l'erreur en string pour analyse
        const fullErrorString = JSON.stringify(err).toLowerCase();
        console.log('Full error string:', fullErrorString);
        
        // Afficher le message d'erreur email
        this.toastr.error(
          'This email is already registered. Please use a different email.',
          'Registration Failed',
          {
            timeOut: 5000,
            progressBar: true,
            closeButton: true
          }
        );
      }
    );
  }

}
