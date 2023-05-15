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
    
    
    
    
    


  ],
  exports:[
    HomeComponent,
    QuienesSomosComponent,
    ContactoComponent,    
    RegistroComponent,
    ProfesionalesComponent,
    
    
    
  ],

  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    DashboardModule
    

    
    
    



  ]
})
export class PagesModule {  }
