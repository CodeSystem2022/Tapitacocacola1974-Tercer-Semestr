package enumeracion;
public enum Continentes {
    AFRICA(53,"1.2billones"),
    EUROPA(46,"1.2billones"),
    ASIA(44,"1.2billones"),
    AMERICA(34,"1.2billones"),
    OCEANIA(14,"1.2billones");
    
    
 private final int paises;
 private String habitantes;
 Continentes(int paises, String habitantes){
 this.paises=paises;
 this.habitantes=habitantes;
 }
 
 //Metodo get
 public int getPaisees(){
 return this.paises;
 
 }
 //Metodo get
 public String getHabitantes(){
 return this.habitantes;
 }
         
}
