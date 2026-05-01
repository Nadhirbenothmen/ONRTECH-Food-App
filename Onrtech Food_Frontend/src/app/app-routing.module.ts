import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';
import { UserComponent } from './user/user.component';
import { LoginComponent } from './login/login.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { ForbiddenComponent } from './forbidden/forbidden.component';
import { RegisterConsumerComponent } from './register-consumer/register-consumer.component';
import { Authguard } from './_Auth/auth.guard';

const routes: Routes = [
  { path: "", redirectTo: "/login", pathMatch: "full" },
  { path: "home", component: HomeComponent },
  { path: "admin", component: AdminComponent, canActivate: [Authguard], data: { roles: ['Admin'] } },
  { path: "register", component: RegisterConsumerComponent },
  { path: "user", component: UserComponent, canActivate: [Authguard], data: { roles: ['Consumer','User'] } },
  { path: "login", component: LoginComponent },
  { path: "admin-login", component: AdminLoginComponent },
  { path: "forbidden", component: ForbiddenComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
