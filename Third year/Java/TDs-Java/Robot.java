import java.awt.Color ;

public class Robot {

    /* 
     *  Les attributs de chaque Robot. 
     */

    /** Position du robot */
    protected int x, y ;

    /** Vitesse du robot */
    protected int vx, vy ;

	/** Position ancien du robot */
	protected int ax, ay;

    /** Etat du robot */
    private boolean vivant ;

    /** Sprite (==image) representant le robot */
    private Sprite image ;
    
    /** Plateau sur lequel le robot evolue */
    private Plateau plat ;

    /** Ce robot est-il arrete' ? */
    private boolean arrete ;

	/**Couleur */
	protected Color col;


    /* 
     *  Constructeur de Robot. 
     */

    /** Cree un nouveau robot avec l'image indiquee, a la position indiquee sur le plateau
     *  La vitesse de depart est aleatoire
     */
    public Robot (String nomImage, int init_x, int init_y, Plateau pt, Color col) {
	this.x = init_x ;
	this.y = init_y ;
	this.ax = 0;
	this.ay = 0;
	this.vivant = true ;
	this.vx = this.randomV() ;
	this.vy = this.randomV() ;
	this.plat = pt ;
	this.image = pt.addSprite (nomImage, this.x, this.y) ;
	this.arrete = false ;
	this.col = col;
    }

    /*
     *  Méthodes
     */


    /** Renvoie une valeur de vitesse aleatoire */
    public int randomV() { return (int)(Math.random() * 6) - 3 ; }

    /** Recupere la largeur de l'image du robot */
    public int getLarg() { return this.image.getLarg() ; }

    /** Recupere la hauteur de l'image du robot */
    public int getHaut() { return this.image.getHaut() ; }


    /** Effectue un deplacement elementaire du robot */
    public void bouge() {

	if (this.vivant) {

	    this.x += this.vx ;
	    this.y += this.vy ;
	    	    
	    // Si le robot rejoint un bord de la fenetre, il rebondit et change de direction
	    int futurX = this.x + this.vx ;
	    int futurY = this.y + this.vy ;
	    
	    // Collision avec le bord gauche
	    if (futurX < 0) {
		this.vx = Math.abs(this.vx) ;
		this.vy = this.randomV() ;
		System.out.println("Merde la mur en gauche!");
	    }

	    // Collision avec le bord droit
	    if (futurX + this.getLarg() > this.plat.getLarg()) {
		this.vx = -Math.abs(this.vx) ;
		this.vy = this.randomV() ;
		System.out.println("Merde la mur en droite!");
	    }

	    // Collision avec le bord haut 
	    if (futurY < 0) {
		this.vy = Math.abs(this.vy) ;
		this.vx = this.randomV() ;
		System.out.println("Merde la mur en haut!");
	    }

	    // Collision avec le bord bas
	    if (futurY + this.getHaut() > this.plat.getHaut()) {
		this.vy = -Math.abs(this.vy) ;
		this.vx = this.randomV() ;
		System.out.println("Merde la mur en bas!");
	    }
	}

	// Redessine le robot au nouvel endroit
	// Force a redessiner, meme si le robot n'a pas bouge.
	this.image.moveTo(this.x, this.y) ;
	if ((Math.pow((this.x - this.ax),2) + Math.pow((this.x - this.ax),2)) >= 10 )
	{	
		this.plat.
		plat.drawCircle(this.x, this.y, 2);
		this.ax = this.x;
		this.ay = this.y;}

    }

    
    /** Teste si ce robot est en collision avec le robot 'autre' */
    public void testeCollision(Robot autre) {

	// Pour etre en collision, il faut une intersection sur les X ET sur les Y
	boolean enCollision = ((this.x + this.getLarg() >= autre.x) && (this.x < autre.x + autre.getLarg()) &&
			       (this.y + this.getHaut() >= autre.y) && (this.y < autre.y + autre.getHaut())) ;

	// Si on est en collision avec un robot different de soi-meme, on reagit et l'autre aussi.
	if (this.vivant && autre.vivant && (autre != this) && enCollision) {

	    // Si les deux robots sont deja arretes, on ne fait rien.
	    if (this.arrete && autre.arrete) {}
	    else {
		this.collision(autre) ;
		autre.collision(this) ;
		System.out.println("Oops!!!");
	    }
	}
    }

    /** Arrêter ce robot. */
    public void arreterRobot() {
	this.vx = 0 ;
	this.vy = 0 ;
	this.arrete = true ;
    }

    /** Fait exploser ce robot */
    public void explose() {
	this.image.playSequence(Images.explosion, false) ;
	this.vivant = false ;
    }

    /** Reaction a une collision : on s'arrete */
    public void collision(Robot autre) {
	this.arreterRobot() ;
    }
}
