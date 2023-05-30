import { Component, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common'
import { CarritoService } from 'src/app/service/carrito.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  public totalItem : number = 0;
  public searchTerm : string = '';
  public isSidebarOpen: boolean = false; // Declare and initialize isSidebarOpen property

  constructor(@Inject(DOCUMENT) private document: Document, private carritoService: CarritoService) { }

  ngOnInit(): void {
    this.carritoService.getProfesionales().subscribe(res => {
      this.totalItem = res.length;
    });
  }

  sidebarToggle() {
    // Toggle sidebar function
    this.document.body.classList.toggle('toggle-sidebar');
    this.isSidebarOpen = !this.isSidebarOpen;
  }

  search(event: any) {
    this.searchTerm = (event.target as HTMLInputElement).value;
    console.log(this.searchTerm);
    this.carritoService.search.next(this.searchTerm);
  }
}
