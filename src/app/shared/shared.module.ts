import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './footer/footer.component';
import { NavComponent } from './nav/nav.component';
import { HeaderComponent } from './header/header.component';
import { RouterModule } from '@angular/router';
import { SidebarComponent } from './sidebar/sidebar.component';









@NgModule({
  declarations: [
    FooterComponent,
    NavComponent,
    HeaderComponent,
    SidebarComponent,
    
    
  ],

  exports: [
    FooterComponent,
    NavComponent,
    HeaderComponent,
    SidebarComponent
    
    
  ],

  imports: [
    CommonModule,
    RouterModule,
    
  ]
})
export class SharedModule { }
