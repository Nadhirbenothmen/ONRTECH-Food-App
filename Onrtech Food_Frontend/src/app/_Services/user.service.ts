import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserAuthService } from './user-auth.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {


  baseurl = "http://localhost:8080/";

  requestHeader = new HttpHeaders({ 'No-Auth': 'True' })
  constructor(
    private httpClient: HttpClient,
    private userAuth: UserAuthService
  ) { }


  public login(loginData: any) {
    return this.httpClient.post(this.baseurl + "authenticate", loginData, { headers: this.requestHeader });
  }


  public forUser() {
    return this.httpClient.get(this.baseurl + "forUser", { responseType: 'text' });
  }


  public forAdmin() {
    return this.httpClient.get(this.baseurl + "forAdmin", { responseType: 'text' });
  }


  public roleMatch(allowedRoles: any): boolean {
    let isMatch = false;
    const userRoles: any = this.userAuth.getRoles()
    if (userRoles != null && userRoles) {
      for (let i = 0; i < userRoles.length; i++) {
        for (let j = 0; j < allowedRoles.length; j++) {
          if (userRoles[i].roleName == allowedRoles[j]) {
            isMatch = true;
            return isMatch;
          }
        }
      }
    }
    return isMatch;


  }

  public registerNewUser(user: any) {
    return this.httpClient.post(this.baseurl + "registerNewUser", user);
  }

  public getConsumers() {
    return this.httpClient.get(this.baseurl + "consumers");
  }

  public activateUser(userName: string) {
    return this.httpClient.put(this.baseurl + "activate/" + userName, {});
  }

  public deleteUser(userName: string) {
    return this.httpClient.delete(this.baseurl + "deleteUser/" + userName, { responseType: 'text' });
  }
}
