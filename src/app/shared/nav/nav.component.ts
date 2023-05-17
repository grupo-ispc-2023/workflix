import { Component, OnInit, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common'


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
  
})
export class NavComponent implements OnInit {

  constructor(@Inject(DOCUMENT) private document: Document) { }
  isSidebarOpen: boolean = false;
  ngOnInit(): void {
  }
  sidebarToggle()
  {
    //toggle sidebar function
    this.document.body.classList.toggle('toggle-sidebar');
    this.isSidebarOpen = !this.isSidebarOpen;
  }

  

  
}
