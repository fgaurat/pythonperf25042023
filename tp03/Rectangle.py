
class Rectangle:

    def __init__(self,longueur,largeur):
        self.__longueur = longueur # _Rectangle__longueur
        self.__largeur = largeur
    
    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur

    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur

    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    def __del__(self):
        print("del rectangle")