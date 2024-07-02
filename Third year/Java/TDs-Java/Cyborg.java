public class Cyborg extends Robot{
    private boolean vivant ;

    /** Sprite (==image) representant le cyborg */
    private Sprite image ;
    
    /** Plateau sur lequel le cyborg evolue */
    private Plateau plat ;

    /** Ce cyborg est-il arrete' ? */
    private boolean arrete ;

    private int nombreCollisions;

    /** Nombre de collisions subies */

    private int maxCollisions;

    /**Limite de collisions */

    /** Cyborg constructor */

    public Cyborg (String nomImage, int init_x, int init_y, Plateau pt, int init_max, , Color col) {
	super(nomImage, init_x, init_y, pt, col);
    this.maxCollisions = init_max;
    this.nombreCollisions = 0;
    }
    
    public void collision(Robot autre) {
	if (this.nombreCollisions < this.maxCollisions){
        this.vx = - this.vx;
        this.vy = - this.vy;
        this.nombreCollisions = this.nombreCollisions + 1;
    } else {
        this.explose() ;
    }
    }
}