import java.util.*;
public class InsectActivite extends Activite{
    protected String insect;

    protected String ferocite;

    public static int nbrInsect = 0;

    public InsectActivite(String nom, ArrayList <Integer> semaine, int cout, Parcelles plot, String insect,String ferocite){
        super(nom,semaine,cout,plot);
        this.insect = insect;
        this.ferocite = ferocite;
        nbrInsect += 1;
    }

    public int eau(){
        return (int) (100.00*this.plot.superficie);
    };

    public int aidEstimer(){
        return (int) (plot.superficie*1000.00 + 2000.00);
    };
}