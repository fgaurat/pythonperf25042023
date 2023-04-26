
class Rectangle:

    def __init__(self,longueur,largeur):
        self.__longueur = longueur # _Rectangle__longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self,longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self,largeur):
        self.__largeur = largeur

    def surface(self):
        return self.__longueur*self.__largeur
    
    def __del__(self):
        print("del rectangle")