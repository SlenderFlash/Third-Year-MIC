import java.util.*;
public class RecoltActivite extends Activite{
    protected String timing;

    protected String materiel;

    public static int nbrRecolt = 0;

    public RecoltActivite(String nom, 
    ArrayList <Integer> semaine, int cout, Parcelles plot, String timing,String materiel){
        super(nom,semaine,cout,plot);
        this.timing = timing;
        this.materiel = materiel;
        nbrRecolt += 1;
    }

    public int eau(){
        return (int) (200.00*this.plot.superficie);
    };
}