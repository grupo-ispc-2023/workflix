import { Component, OnInit } from '@angular/core';
import { Tarjeta } from 'src/assets/datos-profesionales/tarjetas';
import { ApiService } from 'src/app/service/api.service';
import { CarritoService } from 'src/app/service/carrito.service';

@Component({
  selector: 'app-profesionales',
  templateUrl: './profesionales.component.html',
  styleUrls: ['./profesionales.component.css'],
})
export class ProfesionalesComponent implements OnInit {
  public profesionalesList: any[] = [];
  public filterProfesion: any[] = [];
  searchKey: string = '';
  lista: Tarjeta[] = [];

  constructor(private api: ApiService, private carritoService: CarritoService) {}

  ngOnInit(): void {
    this.api.getProfesional().subscribe((res: any[]) => {
      this.profesionalesList = res.map((item: any) => ({
        ...item,
        quantity: 1,
        total: item.price,
      }));

      this.filterProfesion = [...this.profesionalesList];
      this.lista = [...this.profesionalesList];
    });

    this.carritoService.search.subscribe((val: any) => {
      this.searchKey = val;
    });
  }

  agregarcarrito(item: any) {
    this.carritoService.agregarCarrito(item);
  }

  filter(profesion: string) {
    if (profesion === '') {
      this.filterProfesion = [...this.profesionalesList];
    } else {
      this.filterProfesion = this.profesionalesList.filter(
        (item: any) => item.profesion === profesion
      );
    }
  }
}
