import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api.service';
import { CarritoService } from 'src/app/service/carrito.service';

@Component({
  selector: 'app-profesionales',
  templateUrl: './profesionales.component.html',
  styleUrls: ['./profesionales.component.css']
})
export class ProfesionalesComponent implements OnInit {
  public profesionalesList: any[] = [];
  public filterProfesion: any[] = [];
  public searchKey: string = '';
  public filtroActivo: string = '';

  constructor(private api: ApiService, private carritoService: CarritoService) { }

  ngOnInit(): void {
    this.api.getProfesional().subscribe(res => {
      this.profesionalesList = res;
      this.filterProfesion = res;
    });
    this.carritoService.search.subscribe((val: any) => {
      this.searchKey = val;
    });
  }

  agregarcarrito(item: any): void {
    this.carritoService.agregarCarrito(item);
  }

  filter(profesion: string): void {
    this.filterProfesion = this.profesionalesList.filter((a: any) => {
      if (a.profesion === profesion || profesion === '') {
        return a;
      }
    });
    this.filtroActivo = profesion; // Actualiza el filtro activo
  }
}
