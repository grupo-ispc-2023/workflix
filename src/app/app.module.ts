import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { PagesModule } from './layouts/pages/pages.module';
import { SharedModule } from './shared/shared.module';
import { FormularioProfesionalesClientesComponent } from './layouts/pages/formulario-profesionales-clientes/formulario-profesionales-clientes.component';





@NgModule({
  declarations: [
    AppComponent,
    FormularioProfesionalesClientesComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    PagesModule,
    SharedModule,
    
    
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
