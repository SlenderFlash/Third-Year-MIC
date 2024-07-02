import java.util.*;
public abstract class Activite{
    protected String nom;

    protected ArrayList <Integer> semaine;

    protected int cout;

    protected Parcelles plot;

    public static int nbrActivite = 0;

    public Activite (String nom, ArrayList <Integer> semaine, int cout, Parcelles plot){
        this.nom = nom;
        this.semaine = semaine;
        this.cout = cout;
        this.plot = plot;
        nbrActivite += 1;
        this.plot.listActivite.add(this);
    };

    public abstract int eau();

    public int aidEstimer(){
        return (int) (plot.superficie * 1000.00);
    };
}