import { ActivatedRouteSnapshot, CanActivate, CanActivateFn, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { UserAuthService } from '../_Services/user-auth.service';
import { UserService } from '../_Services/user.service';
import { Injectable } from '@angular/core';


@Injectable()
export class Authguard implements CanActivate {

  constructor(
    private userAuthService: UserAuthService,
    private router: Router,
    private userService: UserService
  ) { }
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    if (this.userAuthService.getToken() != null) {
      const role = route.data["roles"] as Array<string>;

      if (role) {
        const match = this.userService.roleMatch(role);
        if (match) {
          return true;
        } else {
          this.router.navigate(['/forbidden'])
          return false;
        }
      }
    }
    this.router.navigateByUrl('/login');
    return false;

  }
};
