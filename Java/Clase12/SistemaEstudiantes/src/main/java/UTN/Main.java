package UTN;

import UTN.conexion.Conexion;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        var conexion = Conexion.getConnection();
        if(conexion != null)
            System.out.println("Conexion exitosa "+conexion);
        else
            System.out.println("error al conectarse");

        }//fin main


}//fin clase