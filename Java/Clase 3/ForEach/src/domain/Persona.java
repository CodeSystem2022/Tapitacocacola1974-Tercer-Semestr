package domain;

public class Persona {
    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}';
    }
    
    public String GetNombre(){
    return nombre;
            }
    public void setNombre (String nombre){
    this.nombre=nombre;
    }
}
