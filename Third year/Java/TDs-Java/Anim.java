/** Boucle principale de la simulation */

public class Anim {

    /** Effectue une pause de la duree indiquee en millisecondes */
    public static void pause(int duree) {
	try {
	    Thread.currentThread().sleep(duree) ;
	} catch (InterruptedException e) {
	} 
    }

    /** Boucle principale */
    public void go() {
	
	Plateau plat ;
	Robot[] robots ;

	plat = new Plateau(800, 600) ;
	robots = new Robot[4] ;

	robots[0] = new Robot("Images/mini1.png", 80, 100, plat, Color.black) ; 
	robots[1] = new Robot("Images/mini2.png", 480, 250, plat, Color.magenta) ; 
	robots[2] = new Robot("Images/mini3.png", 280, 400, plat, Color.red) ;
	robots[3] = new Robot("Images/mini4.png", 480, 400, plat, Color.blue) ;


	// On repete la boucle d'animation sans arret
	while (true) {

	    // On fait evoluer chaque robot
	    for (int i = 0 ; i < robots.length ; i++) {
		robots[i].bouge () ;
	    }

	    // Puis on teste les collisions deux a deux
	    for (int i = 0 ; i < robots.length ; i++) {
		for (int j = i+1 ; j < robots.length ; j++) {
		    robots[i].testeCollision(robots[j]) ;
		}
	    }

	    // Petite pause
	    java.awt.Toolkit.getDefaultToolkit().sync(); // Sinon l'animation est saccadée - probablement à cause du Window Manager.
	    Anim.pause(12) ;
	}

    }
    
	public void goCyborg() {
	
	Plateau plat ;
	Cyborg[] Cyborgs ;

	plat = new Plateau(800, 600) ;
	Cyborgs = new Cyborg[4] ;

	Cyborgs[0] = new Cyborg("Images/mini1.png", 80, 100, plat, 50) ; 
	Cyborgs[1] = new Cyborg("Images/mini2.png", 480, 250, plat, 50) ; 
	Cyborgs[2] = new Cyborg("Images/mini3.png", 280, 400, plat, 50) ;
	Cyborgs[3] = new Cyborg("Images/mini4.png", 480, 400, plat, 50) ;


	// On repete la boucle d'animation sans arret
	while (true) {

	    // On fait evoluer chaque Cyborg
	    for (int i = 0 ; i < Cyborgs.length ; i++) {
		Cyborgs[i].bouge () ;
	    }

	    // Puis on teste les collisions deux a deux
	    for (int i = 0 ; i < Cyborgs.length ; i++) {
		for (int j = i+1 ; j < Cyborgs.length ; j++) {
		    Cyborgs[i].testeCollision(Cyborgs[j]) ;
		}
	    }

	    // Petite pause
	    java.awt.Toolkit.getDefaultToolkit().sync(); // Sinon l'animation est saccadée - probablement à cause du Window Manager.
	    Anim.pause(12) ;
	}

    }

    public static void main(String[] args) {
	Anim an = new Anim() ;
	Images.init () ;
	an.goCyborg () ;
    }

}
