package excepciones;

public class OperacionExcepcion extends RuntimeException {
    //Contructor
    public OperacionExcepcion(String mensaje){
    
        super(mensaje);
    }
}
