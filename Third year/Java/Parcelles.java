import java.util.*;


public class Parcelles {
    protected String section;

    protected int numero;

    protected double superficie;

    protected ArrayList <Activite> listActivite;

    public Parcelles (String section, int numero, double superficie){
        this.section = section;
        this.numero = numero;
        this.superficie = superficie;
        this.listActivite = new ArrayList<Activite>();
    };

    public String toString(){
        return "Parcelle : Section :"+this.section+", numero :"+ this.numero;
    };

    public void setNumParcelle(int num) throws ExceptionNumNegatif{
        if (num < 0) {
            throw new ExceptionNumNegatif("Le numero de parcelle ne peux pas etre negatif!");
        } else
        {
            this.numero = num;
        }
    };

    public Activite plusCherActivite(){
        Activite max = this.listActivite.get(0);
        Iterator<Activite> ind = this.listActivite.iterator();
        while(ind.hasNext()){
            Activite monActivite = ind.next();
            if (monActivite.cout > max.cout){
                max = monActivite;
            };
        };
        return max;
    }
}



