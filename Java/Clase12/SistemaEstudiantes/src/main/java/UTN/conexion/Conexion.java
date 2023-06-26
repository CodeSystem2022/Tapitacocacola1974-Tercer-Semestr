package UTN.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion= null;
        //variables para conectarnos a la base de datos
        var baseDatos="estudiantes2023";
        var url="jdbc:mysql://localhost:3306/"+baseDatos;
        var usuario="root";
        var password="matiitas";

        //cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrió un error en la conexión: "+e.getMessage());
        }//fin catch
        return conexion;
    }//Fin método getConnection
<<<<<<< Updated upstream
}
=======
}
>>>>>>> Stashed changes
