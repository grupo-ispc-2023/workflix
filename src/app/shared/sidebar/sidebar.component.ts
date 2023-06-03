import { Component, HostListener } from '@angular/core';
import { ScrollingService } from 'src/app/scrolling.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  
  constructor(private scrollingService: ScrollingService) { }

  onClickEnlace() {
    this.scrollingService.scrollToTop();
  }

  onClickPosition() {
    const destination = 500; // La posición de destino deseada
    this.scrollingService.scrollTo(destination);
  }
//  isComponentVisible: boolean = true;

//  @HostListener('window:scroll', [])
//  onWindowScroll() {
//    // Lógica para determinar si se debe ocultar el componente
//    if (window.pageYOffset > 100) {
//      this.isComponentVisible = false;
//    } else {
//      this.isComponentVisible = true;
//    }
//  }


}
