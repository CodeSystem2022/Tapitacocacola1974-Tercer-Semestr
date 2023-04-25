package Test;

import enumeracion.Continentes;
import enumeracion.Dias;
import static enumeracion.Dias.MIERCOLES;

public class TestEnumeracion {
    public static void main(String[] args) {
      //  System.out.println("Dia 1: "+Dias.DOMINGO);
       // indicarDiaSemana(Dias.DOMINGO);
        System.out.println("Contienentes no. 4: "+Continentes.AMERICA);   
        System.out.println("No. de habitantes en el 4to. contienentes: "+Continentes.AMERICA.getHabitantes());
    }
    
    private static void indicarDiaSemana(Dias dias){
    switch(dias){
        case LUNES:
            System.out.println("Primer dia de la semana ");
            break;
        case MARTES:
            System.out.println("Segundo dia de la semana");
            break;
         case MIERCOLES:
            System.out.println("Tercer dia de la semana");
            break;
            case JUEVES:
            System.out.println("Cuarto dia de la semana");
            break;
            case VIERNES:
            System.out.println("Quinto dia de la semana");
            break;
            case SABADO:
            System.out.println("Sexto dia de la semana");
            break;
            case DOMINGO:
            System.out.println("Septimo dia de la semana");
            break;
            default:
                System.out.println("No eligio ningun dia de la semana...");
                
            
            
            
    }     
    }
}
