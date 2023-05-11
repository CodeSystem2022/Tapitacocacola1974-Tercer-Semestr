package test;
import domain.*;
public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado=new Escritor("Juan",5000,TipoEscritura.CLASICO);
         //System.out.println("empleado= "+empleado);
         System.out.println(empleado.obtenerDetalle());
         //empleado.getTipoEscritura(); //no se puede hacer
         //Downcasting
       //  ((Escritor)empleado).getTipoEscritura();//Tenemos dos opciones esta es una
         Escritor escritor=(Escritor)empleado;//segunda opcion
         escritor.getTipoEscritura();
    
    //Upcasting
    Empleado empleado2= escritor;
    System.out.println(empleado2.obtenerDetalle());
    }
}
