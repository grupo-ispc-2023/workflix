import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


import { HomeComponent } from './layouts/pages/home/home.component';
import { QuienesSomosComponent } from './layouts/pages/quienes-somos/quienes-somos.component';
import { ContactoComponent } from './layouts/pages/contacto/contacto.component';
import { LoginComponent } from './layouts/pages/login/login.component';
import { RegistroComponent } from './layouts/pages/registro/registro.component';
import { ProfesionalesComponent } from './layouts/pages/profesionales/profesionales.component';
import { AdminComponent } from './dashboard/admin/admin.component';
import { PerfilUsuarioComponent } from './layouts/pages/perfil-usuario/perfil-usuario.component';
import { NotificacionesComponent } from './layouts/pages/notificaciones/notificaciones.component';
import { PreguntasFrecuentesComponent } from './layouts/pages/preguntas-frecuentes/preguntas-frecuentes.component';
import { PagosComponent } from './layouts/pages/pagos/pagos.component';
import { FavoritosComponent } from './layouts/pages/favoritos/favoritos.component';
import { CarritoComponent } from './shared/carrito/carrito.component';
import { UsuarioComponent } from './dashboard/usuario/usuario.component';



const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'quienes-somos', component: QuienesSomosComponent },
  { path: 'notificaciones', component: NotificacionesComponent},
  { path: 'preguntasFrecuentes', component: PreguntasFrecuentesComponent},
  { path: 'pagos', component: PagosComponent},
  { path: 'favoritos', component: FavoritosComponent},
  { path: 'contacto', component: ContactoComponent },
  { path: 'dashboard', component: AdminComponent },
  { path: 'dashboardUsuario', component: UsuarioComponent },
  { path: 'login', component: LoginComponent },
  { path: 'perfilUsuario', component: PerfilUsuarioComponent },
 
  { path: 'registro', component: RegistroComponent },
  { path: 'profesionales', component: ProfesionalesComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Ruta por defecto
  { path: 'carrito', component: CarritoComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]


})
export class AppRoutingModule { }
