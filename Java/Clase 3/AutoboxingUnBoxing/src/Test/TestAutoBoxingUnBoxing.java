package Test;

public class TestAutoBoxingUnBoxing {
    public static void main(String[] args) {
        //clases envolventes o wrapper
            /*
    clases envolventes de toopos primitivos
    int=clase envolventes es integer
    long
    float
    double
    boolean
    byte
    char
    short
    */
    int enteroPrim=10; //tipo primitivo
    System.out.println("enteroPrim= "+ enteroPrim);
    Integer entero = 10; //tipo objeto con la clase integer
    
   System.out.println("entero= "+entero.doubleValue());//AutoBoxing es el cambio de un numero a diferentes clases
   int entero2=entero;//UnBoxing
        System.out.println("entero2= "+entero2);
    }        
            
}
