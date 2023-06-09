//josefina Grande-Joaquin Avaro Acosta
import java.util.Scanner;

public class ClaculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){ //ciclo infinito
            System.out.println("*******Aplicacion Calculadora *******");
            mostrarMenu();

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    System.out.print("Digitenel valor para el operando1: ");
                    var operando1 = Integer.parseInt(entrada.nextLine());
                    System.out.print("Digitenel valor para el operando2: ");
                    var operando2 = Integer.parseInt(entrada.nextLine());

                    int resultado;
                    switch (operacion) {
                        case 1 -> {
                            resultado = operando1 + operando2;
                            System.out.println("resultado:" + resultado);
                        }
                        case 2 -> {
                            resultado = operando1 - operando2;
                            System.out.println("resultado de la resta " + resultado);
                        }
                        case 3 -> {
                            resultado = operando1 * operando2;
                            System.out.println("El resultado de la multiplicacion" + resultado);
                        }
                        case 4 -> {
                            resultado = operando1 / operando2;
                            System.out.println("resultado de la division " + resultado);
                        }
                        default -> System.out.println("Opcion erronea:" + operacion);

                    } //fin switch

                } //fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta Pronto...");
                    break; //rompe el ciclo y sale
                } else {
                    System.out.println("opcion erronea" + operacion);
                }
                //imprimimos un salto de linea antes de repetir el menu
            } catch (Exception e){ //fin del try
                System.out.println("Ocurrio un error" + e.getMessage());
                System.out.println();
            }
        } //fin while
    }//fin main

    private static void mostrarMenu(){
        //mostramos el menu
        System.out.println("""
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Salir
                """);
        System.out.print("Operacion a realizar?");
    }
} //fin clase

