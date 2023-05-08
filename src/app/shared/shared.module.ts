import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './footer/footer.component';
import { NavComponent } from './nav/nav.component';
import { HeaderComponent } from './header/header.component';
import { RouterModule } from '@angular/router';






@NgModule({
  declarations: [
    FooterComponent,
    NavComponent,
    HeaderComponent,
    
  ],

  exports: [
    FooterComponent,
    NavComponent,
    HeaderComponent,
    
    
  ],

  imports: [
    CommonModule,
    RouterModule,
    
  ]
})
export class SharedModule { }
