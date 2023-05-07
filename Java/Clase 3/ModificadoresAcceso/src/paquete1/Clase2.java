package paquete1;

class Clase2{
    String atributoDefault="Valor del atributo defaul";

   // Clase2() {
     //   System.out.println("Contructor Default");
        
    //}
    public Clase2(){
        super();
        this.atributoDefault="Modificacion del atributo defaul";
        System.out.println("atributodefaul = "+this.atributoDefault);
        this.metodoDefault();
    }
    void metodoDefault(){
        System.out.println("Metodo default");
    }
    
}
