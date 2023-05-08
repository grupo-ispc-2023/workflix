import { Component } from '@angular/core';
import { FormBuilder, MinValidator, Validators } from '@angular/forms';
import { FormGroup } from '@angular/forms';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  
  forma!:FormGroup; // Declaración de la variable 'forma'
  
//------------------------------------------------------------------------------------
  get usuarioNoValido(){


    return this.forma.get('usuario')?.invalid && this.forma.get('usuario')?.touched;

  }

  

  get password1NoValido(){

    return this.forma.get('password1')?.invalid && this.forma.get('password1')?.touched;

  }

  

//-----------------------------------------------------------------------------------

  constructor(private fb:FormBuilder){

    this.crearFormulario()

  }

  crearFormulario(){
    this.forma = this.fb.group({
      usuario:['', [Validators.required , Validators.minLength(4)]],
      
      
      password1:['', [Validators.required , Validators.minLength(6)]],
     

    }, {
      
      
    }
    
    )
  }

  guardar(){
    console.log(this.forma);

    

    if (this.forma.invalid) {

      return Object.values(this.forma.controls).forEach(control=> {

        control.markAllAsTouched()

      })

    }

  }

  limpiar(){

  this.forma.reset();

  }

  


  

}
