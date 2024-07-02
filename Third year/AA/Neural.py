import numpy as np
class Parameter() :
    def __init__(self,shape) :
        self.shape=shape
        np.random.seed(42)
        self.grad=np.zeros(self.shape)
        self.size=self.grad.size
        self.data=np.random.randn(self.size).reshape(self.shape)

class Generic() : 
    def __init__(self) :
        self.list_params=[] # Liste des paramètres
        self.save=None # Objet pour sauver des infos dans le forward
    def forward(self,x) : 
        # calcul du forward, x=x_s est le vecteur des donnees d'entrees
        # Cette fonction rend  y=x_{s+1} qui est le vecteur des donnees de sortie
        self.save=np.copy(x)
        y=None
        return y
    def backward(self,hat_y) :  
        # retropropagation du gradient sur la couche, 
        #hat_y est le vecteur du gradient de x_{s+1}
        #Cette fonction rend :
        #hat_x, le vecteur du gradient de x_s
        #hat_p, le vecteur du gradient par rapport aux paramètres, ils sont rangés dans p.grad pour tout p dans list_params
        hat_x=None
        return hat_x
 

class Arctan():
    def __init__(self) :
        self.list_params=[] 
        self.save=None 
    def forward(self,x) : 
        self.save=np.copy(x)
        y = np.arctan(x)
        return y
    def backward(self,hat_y) :  
        hat_x=hat_y/(1+self.save**2)
        return hat_x
    
class Sigmoid() : 
    def __init__(self) :
        self.list_params=[] 
        self.save=None 
    def forward(self,x) : 
        self.save = np.copy(x)
        y = 1/(1+np.e**(-self.save))
        return y
    def backward(self,hat_y) :  
        hat_x = hat_y*np.e**(-self.save)/(1+np.e**(-self.save))**2
        return hat_x
     
class Dense() : 
    def __init__(self,nb_entree,nb_sortie):
            A=Parameter((nb_sortie,nb_entree))
            b=Parameter((nb_sortie,1))
            self.list_params=[A,b] # Liste des paramètres
            self.save=None # Objet pour sauver des infos dansleforwar
    def forward(self,x):
            self.save=np.copy(x)
            (A,b)=[p.data for p in self.list_params]
            return A@x + b
    def backward(self,hat_y) :
            x=self.save
            (A,b)=[p.data for p in self.list_params]
            hat_A=hat_y@x.T
            hat_b=np.sum(hat_y,axis=1)
            hat_x=A.T@hat_y
            self.list_params[0].grad=hat_A
            self.list_params[1].grad=hat_b
            for p in self.list_params :
                p.grad=p.grad.reshape(p.shape)
            return hat_x

class Loss_L2():
    def __init__(self,D):
        self.save = None
        self.data = np.copy(D)
        self.list_params = []
    def forward(self,x):
        self.save = np.copy(x)
        return np.linalg.norm(x - self.data)**2/2
    def backward(self,hat_y):
        return hat_y*(self.save - self.data)
    
class Sequential:
    def __init__(self, list_layers):
        self.list_params = []
        self.save = None
        self.list_layers = list_layers
        for couche in list_layers:
            self.list_params += couche.list_params

    def forward(self, x):
        self.save = np.copy(x)
        z = np.copy(x)
        for couche in self.list_layers:
            z = couche.forward(z)
        return z

    def backward(self, hat_y):
        z = np.copy(hat_y)
        for l in reversed(self.list_layers):
            z = l.backward(z)
        return z