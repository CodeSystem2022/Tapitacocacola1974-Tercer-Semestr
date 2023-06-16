import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        List<Persona> personas = new ArrayList<>();

        var salir = false;
        while (!salir) {
            mostrarMenu();
            try {
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e) {
                System.out.println("Ocurrió un error: " + e.getMessage());
            }
        }
    }

    private static void mostrarMenu() {
        System.out.println("""
                **** Listado de personas ****
                1. Agregar
                2. Listar
                3. Salir
                """);
        System.out.println("Digite una de las opciones:");
    }

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        boolean salir = false;

        switch (opcion) {
            case 1 -> {
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var telefono = entrada.nextLine();
                System.out.print("Digite el correo: ");
                var email = entrada.nextLine();
                var persona = new Persona(nombre, telefono, email);
                personas.add(persona);
                System.out.println("La lista tiene: " + personas.size() + " elementos");
            }
            case 2 -> {
                System.out.println("Listado de personas: ");
                personas.forEach(System.out::println);
            }
            case 3 -> {
                System.out.println("Hasta Pronto...");
                salir = true;
            }
            default -> System.out.println("Opcion incorrecta: " + opcion);
        }
        return salir;
    }
}