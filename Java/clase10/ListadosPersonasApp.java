
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadosPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //definimos la lista fuera del ciclo while
        List <Persona>personas = new ArrayList<>();
        //empezamos con el menu
        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada,personas);
            } catch(Exception e){
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
            System.out.println();
        }//fin while

    }//fin de main

    public static void mostrarMenu() {
        //mostramos las opciones
        System.out.print("""
                ****Listado de Personas****
                1-Agregar
                2-Listar
                3-Salir
                """);
        System.out.println("digite una de las opciones");
    }//fin metodo mostrar menu

    private static boolean ejecutarOperacion(Scanner entrada,List<Persona>personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //revisamos la opcion a partir de un switch
        switch (opcion){
            case 1 ->{//agregar persona a la lista
                System.out.println("digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.println("digite el telefono: ");
                var telefono = entrada.nextLine();
                System.out.println("digite el email: ");
                var email = entrada.nextLine();
                var persona = new Persona(nombre,telefono,email);
                        //Agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos");


            }
            case 2 ->{//listar personas
                System.out.println("listado de personas");
                //mejoras con lambda y metodos de referencia
                //personas.forEach((persona)-> System.out.println(persona));
                personas.forEach(System.out::println);
            }
            case 3 ->{//salir del ciclo
                System.out.println("Hasta pronto: ");
                salir = true;

            }

            default -> System.out.println("opcion incorrecta: "+ opcion);
        }//fin del switch;
        return salir;
    }//fin funcion ejecutaroperacion

}