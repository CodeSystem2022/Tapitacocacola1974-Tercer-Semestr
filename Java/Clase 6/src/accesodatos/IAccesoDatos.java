package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO=10;
    //metodo insertar es abstaracto sin cuerpo
    void insertar();
    void listar();
    void actualizar();
    void eliminar();
}
