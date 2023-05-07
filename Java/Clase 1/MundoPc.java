
package mundopc;

import ar.com.system2023.mundopc.*;



public class MundoPc {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13);
        Teclado tecladoHP = new Teclado("Bluethoo","Hp");
        Raton ratonHP = new Raton("Bluethoo","hp");
        Computadora computadoraHP = new Computadora("computadora HP", monitorHP,tecladoHP,ratonHP);
        //creamos otro objeto
        Monitor monitorGamer = new Monitor("Gamer",32);
        Teclado tecladoGamer = new Teclado("Bluethoo","Gamer");
        Raton ratonGamer = new Raton("Bluethoo","Gamer");
        Computadora computadoraGamer = new Computadora("computadora Gamer", monitorGamer,tecladoGamer,ratonGamer);
        Orden orden1 = new Orden();
        orden1.agregarComputadora(computadoraHP);
       orden1.agregarComputadora(computadoraGamer);
       orden1.mostrarOrden();
    }
}
