package Test;

import domain.*;

public class TestIntanceOf {
    public static void main(String[] args) {
        Empleado empleado1=new Empleado("Juan",1000);
       //determinarTipo(empleado1);
        empleado1=new Gerente("jose",5000,"Sistemas");
        determinarTipo(empleado1);
    }
    public static void determinarTipo(Empleado empleado){
        if (empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            Gerente gerente =(Gerente)empleado;
            System.out.println("gerente= "+empleado);
            
    }else if(empleado instanceof Empleado){
            System.out.println("Es de tipo empleado");
            //Gerente gerente =(Gerente)empleado;
            //System.out.println("gerente= "+gerente.getDepartamento());
            
    }else  if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
    }
        
    }
    
}
