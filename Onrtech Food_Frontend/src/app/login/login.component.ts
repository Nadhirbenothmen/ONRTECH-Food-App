import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { UserService } from '../_Services/user.service';
import { UserAuthService } from '../_Services/user-auth.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  showPassword: boolean = false;

  constructor(
    private userService: UserService,
    private userAuthService: UserAuthService,
    private router: Router,
    private toastr: ToastrService
  ) { }
  
  ngOnInit(): void {
  }

  togglePasswordVisibility(): void {
    this.showPassword = !this.showPassword;
  }


  login(loginForm: NgForm) {
    this.userService.login(loginForm.value).subscribe(
      (res: any) => {
        console.log(res.jwtToken);
        console.log(res.user.role);
        
        const role = res.user.role[0];
        
        // Bloquer les admins sur le login utilisateur
        if (role.roleName === "Admin") {
          this.toastr.error(
            'Please use the admin login portal to access your account.',
            'Wrong Login Portal',
            { timeOut: 5000, progressBar: true, closeButton: true }
          );
          return;
        }
        
        // Si c'est un utilisateur, autoriser la connexion
        this.userAuthService.setToken(res.jwtToken);
        this.userAuthService.setRoles(res.user.role);
        localStorage.setItem('userName', res.user.userName);
        
        this.toastr.success(
          `Welcome back, ${res.user.userName}!`,
          'Login Successful',
          { timeOut: 3000, progressBar: true }
        );
        
        this.router.navigate(["/user"]);
      },
      err => {
        console.error('Login error:', err);
        
        // Handle different error responses
        if (err.error && err.error.error) {
          const errorType = err.error.error;
          const errorMessage = err.error.message;
          
          switch (errorType) {
            case 'user_disabled':
              this.toastr.warning(
                'Your account is not activated yet. Please wait for admin approval.',
                'Account Not Activated',
                { timeOut: 6000, progressBar: true, closeButton: true }
              );
              break;
              
            case 'invalid_credentials':
              this.toastr.error(
                'The username or password you entered is incorrect. Please try again.',
                'Invalid Credentials',
                { timeOut: 5000, progressBar: true, closeButton: true }
              );
              break;
              
            case 'authentication_error':
              this.toastr.error(
                'The username or password you entered is incorrect. Please try again.',
                'Authentication Error',
                { timeOut: 5000, progressBar: true, closeButton: true }
              );
              break;
              
            default:
              this.toastr.error(
                'Unable to login. Please try again later.',
                'Login Failed',
                { timeOut: 5000, progressBar: true, closeButton: true }
              );
          }
        } else if (err.status === 0) {
          // Network error
          this.toastr.error(
            'Unable to connect to the server. Please check your connection.',
            'Connection Error',
            { timeOut: 5000, progressBar: true, closeButton: true }
          );
        } else {
          // Generic error
          this.toastr.error(
            'An unexpected error occurred. Please try again.',
            'Login Failed',
            { timeOut: 5000, progressBar: true, closeButton: true }
          );
        }
      }
    );
  }

}
