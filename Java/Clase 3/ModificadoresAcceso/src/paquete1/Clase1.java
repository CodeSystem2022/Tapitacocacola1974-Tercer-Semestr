package paquete1;

public class Clase1 {
        public String atributoPublic = "Valor atributo publico";  
        protected String atributoProtected="Valor atributo protected";
                public Clase1(){
            System.out.println("contructor public");
        }
       protected Clase1(String atributoPublico){
           System.out.println("Contructor protected");
       }
        public void metoPublico(){
            System.out.println("Metodo publico");
        }
        protected void metodoProtected(){
            System.out.println("Metodo protected");
                }
        
}

