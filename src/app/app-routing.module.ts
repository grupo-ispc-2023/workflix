import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


import { HomeComponent } from './layouts/pages/home/home.component';
import { QuienesSomosComponent } from './layouts/pages/quienes-somos/quienes-somos.component';
import { ContactoComponent } from './layouts/pages/contacto/contacto.component';
import { LoginComponent } from './layouts/pages/login/login.component';
import { RegistroComponent } from './layouts/pages/registro/registro.component';
import { ProfesionalesComponent } from './layouts/pages/profesionales/profesionales.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'quienes-somos', component: QuienesSomosComponent },
  { path: 'contacto', component: ContactoComponent },
  { path: 'login', component: LoginComponent },
  { path: 'registro', component: RegistroComponent },
  { path: 'profesionales', component: ProfesionalesComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Ruta por defecto
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]


})
export class AppRoutingModule { }
