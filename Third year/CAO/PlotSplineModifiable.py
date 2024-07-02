


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import numpy as np



class DraggablePoints(object):
    def __init__(self, artists,ax,neval,FonctionTrace, tolerance=5):
        
        self.neval = neval
        self.FonctionTrace = FonctionTrace

        ## Lecture des donnees ##
        X = []
        Y = []
        for artist in artists:
            artist.set_picker(tolerance)
            x,y = artist.center
            X+=[x]; Y+=[y]
        X = np.array(X); Y = np.array(Y);
        
        ### Spline
        X_graphe, Y_graphe = self.FonctionTrace(X,Y)        
        ## fin ##
               


        
        self.artists = artists
        self.currently_dragging = False
        self.current_artist = None
        self.offset = (0, 0)
        self.drawing = Line2D(X_graphe,Y_graphe,color='black')
        self.ax = ax
        self.ax.add_line(self.drawing)

        for canvas in set(artist.figure.canvas for artist in self.artists):
            canvas.mpl_connect('button_press_event', self.on_press)
            canvas.mpl_connect('button_release_event', self.on_release)
            canvas.mpl_connect('pick_event', self.on_pick)
            canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        self.currently_dragging = True

    def on_release(self, event):
        self.currently_dragging = False
        self.current_artist = None

    def on_pick(self, event):
        if self.current_artist is None:
            self.current_artist = event.artist
            x0, y0 = event.artist.center
            x1, y1 = event.mouseevent.xdata, event.mouseevent.ydata
            self.offset = (x0 - x1), (y0 - y1)

    def on_motion(self, event):
        if not self.currently_dragging:
            return
        if self.current_artist is None:
            return
        dx, dy = self.offset
        self.current_artist.center = event.xdata + dx, event.ydata + dy
        self.current_artist.figure.canvas.draw()
        X = []
        Y = []
        for artist in self.artists:
            x,y = artist.center
            X+=[x]; Y+=[y]
        X = np.array(X); Y = np.array(Y); 
        
        ### Spline
        X_graphe, Y_graphe = self.FonctionTrace(X,Y)        
        ## fin ##



        self.drawing.set_data(X_graphe,Y_graphe)
#        self.ax.plot(X,Y)



def DrawModifiableSpline(X,Y,courbePeriodique,BSpline):
    """X,Y coordonnées des données (points de contrôle)
    courbePeriodique : 0 ou 1
    BSpline : fonction qui prend en entrée X, Y et courbePeriodique et qui renvoie X_graphe et Y_graphe"""
    ### Pour créer une figure avec des échelles adaptées aux données
    fig, ax = plt.subplots()
    minX = min(X); maxX = max(X); minY = min(Y); maxY = max(Y); LLX = maxX-minX ; LLY = maxY-minY
    ax.set(xlim=[minX-LLX/10, maxX+LLX/10], ylim=[minY-LLY/10, maxY+LLY/10])
    Rc = min([LLX,LLY])/40
    
    ### Création des points modifiables
    circles = []
    for nn in range(len(X)):
        circles+=[patches.Circle((X[nn], Y[nn]), Rc, fc='b', alpha=0.5)]
    # Ajout des points sur la figure    
    for circ in circles:
        ax.add_patch(circ)
    
    ### Creation de la fonction tracé X_graphe Y_graphe en fonction de X, Y
    def FonctionTrace(X,Y):
        return BSpline(X,Y,courbePeriodique)
    
    ### Affichage 
    neval = 200    
    dr = DraggablePoints(circles,ax,neval,FonctionTrace)
    plt.show()
    plt.axis('equal')
    return dr
        




