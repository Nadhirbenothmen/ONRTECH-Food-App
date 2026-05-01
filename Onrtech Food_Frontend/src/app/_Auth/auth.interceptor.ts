import { HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { UserService } from "../_Services/user.service";
import { UserAuthService } from "../_Services/user-auth.service";
import { Router } from "@angular/router";
import { catchError } from "rxjs/operators";
import { Injectable } from "@angular/core";



@Injectable()
export class AuthInterceptor implements HttpInterceptor {

    constructor(
        private userService: UserAuthService,
        private router: Router
    ) { }
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        if (req.headers.get('No-Auth') == "True") {
            return next.handle(req.clone());
        }
        const token = this.userService.getToken();
        req = this.addToken(req, token);
        console.log(req)
        return next.handle(req).pipe(
            catchError(
                (err: HttpErrorResponse) => {
                    console.log(err.status);
                    if (err.status === 401) {
                        this.userService.clear();
                        this.router.navigateByUrl('/login');

                    }
                    return throwError("something went wrong");
                }
            )
        );

    }

    private addToken(request: HttpRequest<any>, token: string) {
        return request.clone({
            setHeaders: {
                Authorization: `Bearer ${token}`
            }
        })
    }

}