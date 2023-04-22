import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { QuienesSomosComponent } from './quienes-somos/quienes-somos.component';
import { ContactoComponent } from './contacto/contacto.component';
import { DashboardComponent } from './dashboard/dashboard.component';



@NgModule({
  declarations: [
    HomeComponent,
    QuienesSomosComponent,
    ContactoComponent,
    DashboardComponent
  ],
  exports:[
    HomeComponent,
    QuienesSomosComponent,
    ContactoComponent,
    DashboardComponent
  ],

  imports: [
    CommonModule
  ]
})
export class PagesModule {  }
