import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Tarjeta } from '../home/datos/tarjetas';
import { tarjetas } from '../home/datos/datos';

@Component({
  selector: 'app-profesionales',
  templateUrl: './profesionales.component.html',
  styleUrls: ['./profesionales.component.css'],
  
})
export class ProfesionalesComponent implements OnInit{

  lista: Tarjeta[] = tarjetas

  constructor() {
    //this.lista = tarjetas
    console.log(this.lista);
  }

  ngOnInit(): void {
    //this.lista = this.lista.filter(t => t.id >=2 );
    this.lista = tarjetas
  }

}
