import { Component, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { CarritoService } from 'src/app/service/carrito.service';
import { ScrollingService } from 'src/app/scrolling.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  public totalItem: number = 0;
  public searchKey: string = '';
  public isSidebarOpen: boolean = false;

  constructor(
    @Inject(DOCUMENT) private document: Document,
    private carritoService: CarritoService,
    private scrollingService: ScrollingService
  ) { }

  ngOnInit(): void {
    this.carritoService.getProfesionales().subscribe(res => {
      this.totalItem = res.length;
    });
  }

  sidebarToggle() {
    this.document.body.classList.toggle('toggle-sidebar');
    this.isSidebarOpen = !this.isSidebarOpen;
  }

  search(event: any) {
    this.searchKey = event.target.value;
    console.log(this.searchKey);
    this.carritoService.search.next(this.searchKey);
  }



  onClickEnlace() {
    this.scrollingService.scrollToTop();
  }
}

