import java.util.*;
public class TD{
    public static void main(String[] args){
        Parcelles plot = new Parcelles("A",3,250);
        
        System.out.println(plot);
        
        ArrayList<Integer> grasshopperdays = new ArrayList<Integer>(){{
            add(2);
            add(3);
            add(4);
            add(5);
        }};
        
        InsectActivite grasshopper = new InsectActivite("Kill Grasshopper", grasshopperdays, 10000,
        plot, "grasshopper", "high");
        
        ArrayList<Integer> locustdays = new ArrayList<Integer>(){{
            add(1);
            add(3);
            add(6);
            add(7);
        }};
        
        InsectActivite locust = new InsectActivite("Kill Locust", locustdays, 5000,
        plot, "locust", "low");

        ArrayList<Integer> wheatdays = new ArrayList<Integer>(){{
            add(4);
            add(8);
        }};

        RecoltActivite wheat = new RecoltActivite("Recolter wheat", wheatdays, 7000,
        plot, "matin", "plower");

        System.out.println(locust.eau());
        System.out.println(wheat.aidEstimer());
        System.out.println(grasshopper.aidEstimer());
        System.out.println(locust.nbrActivite);
        System.out.println(locust.nbrInsect);
        System.out.println(wheat.nbrRecolt);
        System.out.println(plot.plusCherActivite());
        try {plot.setNumParcelle(-4);}  catch (ExceptionNumNegatif e){
            System.err.println("Exception caught: " + e.getMessage());
        };
    }
}