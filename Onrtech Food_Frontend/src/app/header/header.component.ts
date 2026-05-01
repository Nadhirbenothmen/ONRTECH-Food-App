import { Component } from '@angular/core';
import { UserAuthService } from '../_Services/user-auth.service';
import { Router } from '@angular/router';
import { UserService } from '../_Services/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {


  constructor(
    private userAuth: UserAuthService,
    private router: Router,
    public userService: UserService
  ) { }

  public isLoggedIn() {
    return this.userAuth.isLoggedIn();
  }

  public isAuthPage() {
    const currentUrl = this.router.url;
    return currentUrl === '/login' || currentUrl === '/register';
  }

  public isAdminPage() {
    return this.router.url === '/admin';
  }

  public isHomePage() {
    return this.router.url === '/home' || this.router.url === '/';
  }

  public isUserPage() {
    return this.router.url === '/user';
  }

  public isAdmin() {
    return this.userService.roleMatch(['Admin']);
  }

  public isUser() {
    return this.userService.roleMatch(['User']);
  }

  public logout() {
    this.userAuth.clear();
    this.router.navigate(["/login"]);
  }


}
