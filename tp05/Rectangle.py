
class Rectangle:
    
    __cpt=0 # static

    def __init__(self,longueur,largeur):
        self.__longueur = longueur # _Rectangle__longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1
    
    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur

    @property
    def largeur(self)->int:
        return self.__largeur
    
    @largeur.setter
    def largeur(self,largeur:int):
        self.__largeur = largeur

    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt    

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.longueur=}, {self.largeur=}"

        
    def __del__(self):
        print("del rectangle")
        Rectangle.__cpt-=1
    

    def __eq__(self, __value: object) -> bool:
        return self.longueur == __value.longueur and self.largeur == __value.largeur

