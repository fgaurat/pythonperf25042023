from Rectangle import Rectangle

class Carre(Rectangle):
    
    def __init__(self, cote:int):
        print(f"def __init__(self, {cote})")
        super().__init__(cote, cote)
        self.__cote = cote
    
    @property
    def cote(self)->int:
        return self.__cote

    @cote.setter
    def cote(self,cote:int):
        self.__cote = cote
        self.longueur = cote
        self.largeur = cote
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__cote=}"


    def __del__(self):
        print("del Carre")