package Test;
import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificaroesAccesos {
    public static void main(String[] args) {
        Clase1 clase1=new Clase1();
        System.out.print("Clase1= "+clase1.atributoPublic);
        clase1.metoPublico();
        Clase3 claseHija= new Clase3();
        System.out.println("claseHija= "+ claseHija);
    }
}
//java video 7