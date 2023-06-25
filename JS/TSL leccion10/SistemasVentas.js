class Producto{

        static contadorProductos= 0;
        constructor(nombre,precio){
        this._idProducto= ++Producto.contadorProductos;
        this._nombre= nombre;
        this._precio = precio;

    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){
    return `idproducto:${this._idProducto},nombre:${this._nombre}, precio:${this._precio}`;

    // fin de la case Producto
    }
}
class Orden{
        static contadorOrdenes = 0;
        static getMAX_PRODUCTOS(){//SIMULA UNA CONSTANTE    
            return 5;
        }

        constructor(){
            this._idOrden= ++Orden.contadorOrdenes;
            this._productos= [];
            this._contadorProductosAgregados= 0;
        }

        get idOrden(){
            return this._idOrden;
        }

        agregarProductos(Producto){
            if(this._productos.length < Orden.getMAX_PRODUCTOS()){
                this._productos.push(Producto)//tenemos dos tipos de sintaxi:1
                //this._productos[this._contadorProductosAgregados++] = Producto; sintaxis:2
            }
            else{
                console.log("Nose puede agregar mas productos")
            }
        }//fin agregar producto
        caculatTtotal(){
            let totalVentas = 0;
            for(let producto of this._productos){
                totalVentas+= producto.precio
            }// fin ciclo for 
            return totalVentas;
        }// fin del metodo calculartotal

        mostrarOrden(){
            let productoOrden= ' ';
            for (let producto of this._productos){
                productoOrden+= '\n{'+producto.toString()+'}';
            }//fin del ciclo for 

            console.log(`Orden:${this._idOrden},Total:${this.caculatTtotal()},productos:${productoOrden}`);

        }//fin del metodo mostrarOrden 
    }//fin de clase Orden

let producto1 = new Producto('Pantalon',200);
let producto2 = new Producto('Camisa',150); 
let producto3= new Producto('Cinturon',50);
let producto4 = new Producto('Camisa',150); 
let producto5= new Producto('Cinturon',50);
let producto6= new Producto('Billetera',300);
let orden1 = new Orden();
  orden1.agregarProductos(producto1);
  orden1.agregarProductos(producto2);
  orden1.agregarProductos(producto3);
  orden1.agregarProductos(producto4);
  orden1.agregarProductos(producto5);
orden1.agregarProductos(producto6);
  orden1.mostrarOrden();
  orden2 = new Orden();
  orden2.agregarProductos