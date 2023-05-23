import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { QuienesSomosComponent } from './quienes-somos/quienes-somos.component';
import { ContactoComponent } from './contacto/contacto.component';
import { RegistroComponent } from './registro/registro.component';
import { LoginComponent } from './login/login.component';
import { ServiciosComponent } from './home/servicios/servicios.component';
import { ProfesionalesComponent } from './profesionales/profesionales.component';
import { TermsAndConditionsComponent } from './registro/terms-and-conditions/terms-and-conditions.component';
import { FormularioProfesionalesClientesComponent } from './formulario-profesionales-clientes/formulario-profesionales-clientes.component';
import { ReactiveFormsModule, FormsModule, } from '@angular/forms';
import { DashboardModule } from 'src/app/dashboard/dashboard.module';
import { PerfilUsuarioComponent } from './perfil-usuario/perfil-usuario.component';
import { NotificacionesComponent } from './notificaciones/notificaciones.component';
import { PreguntasFrecuentesComponent } from './preguntas-frecuentes/preguntas-frecuentes.component';
import { PagosComponent } from './pagos/pagos.component';
import { FavoritosComponent } from './favoritos/favoritos.component';





@NgModule({
  declarations: [
    HomeComponent,
    QuienesSomosComponent,
    ContactoComponent,    
    RegistroComponent,
    LoginComponent,
    ServiciosComponent,
    ProfesionalesComponent,
    TermsAndConditionsComponent,
    FormularioProfesionalesClientesComponent,
    PerfilUsuarioComponent,
    NotificacionesComponent,
    PreguntasFrecuentesComponent,
    PagosComponent,
    FavoritosComponent,
    
    
    
    
    
    


  ],
  exports:[
    HomeComponent,
    QuienesSomosComponent,
    ContactoComponent,    
    RegistroComponent,
    ProfesionalesComponent,
    NotificacionesComponent
    
    
    
  ],

  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    DashboardModule
    

    
    
    



  ]
})
export class PagesModule {  }
