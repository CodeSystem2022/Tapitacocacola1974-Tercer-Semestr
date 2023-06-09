//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona{   // Clase pedre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre(){
        return this._nombre;
    } 

    get apellido(){
        return this._apellido;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
    // Sobreescribiendo el metodo de la clase padre (objet)
    toString(){ // Regresa un String
        // SE aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        // El metodo que se ejecuta depende sies una referncia de tipo padre o hija
        return this.nombreCompleto();
    }

}
class Empleado extends Persona{//clase hija
    constructor(nombre,apellido,departamento){
        super(nombre,apellido);
        this._departamento=departamento;
    }
get departamento(){
    return this._departamento;
    }

set departamento(departamento){
    this._departamento;
    }
    //Sobreescritura 
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
console.log(persona1.apellido)
persona1.nombre = 'Juan Carlos';
console.log(persona1)
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre)
console.log(persona2.apellido)
//console.log(persona2); 


let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

