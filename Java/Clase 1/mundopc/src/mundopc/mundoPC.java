package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP=new Monitor("HP",13);//IMPORTAR CLASE
        Teclado tecladoHP=new Teclado("Bluetooth","HP");
        Raton ratonHP=new Raton("Bluetooth","HP");
        Computadora computadoraHP=new Computadora("Computadora HP",monitorHP,tecladoHP,ratonHP);
        //Creamos otro objeto
        Monitor monitorGamer=new Monitor("Gamer",32);//IMPORTAR CLASE
        Teclado tecladoGamer=new Teclado("Bluetooth","Gamer");
        Raton ratonGamer=new Raton("Bluetooth","Gamer");
        Computadora computadoraGamer=new Computadora("Computadora HP",monitorGamer,tecladoGamer,ratonGamer);

        Orden orden1=new Orden();//inicializacom el arreglo vacio
        Orden orden2=new Orden();//nueva lista
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        Computadora computadorasVaruas=new Computadora("Computadora de diferentes marcas",monitorHP,tecladoGamer,ratonHP);
        orden2.agregarComputadora(computadorasVaruas);
        
        orden1.mostrarOrdenb();
        orden2.mostrarOrdenb();
    }
}
