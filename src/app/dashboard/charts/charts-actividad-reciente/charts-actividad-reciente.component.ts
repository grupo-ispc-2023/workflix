import { Component, OnInit } from '@angular/core';
import { ClassChartsActividadReciente } from 'src/assets/datos/Class';
import { chartsActividadReciente } from 'src/assets/datos/charts';

@Component({
  selector: 'app-charts-actividad-reciente',
  templateUrl: './charts-actividad-reciente.component.html',
  styleUrls: ['./charts-actividad-reciente.component.css']
})
export class ChartsActividadRecienteComponent  implements OnInit{

  lista: ClassChartsActividadReciente[] = chartsActividadReciente

  constructor() {
    
    
  }

  ngOnInit(): void {
    
    this.lista = chartsActividadReciente
  }
}
