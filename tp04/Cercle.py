


class Cercle:


    def __init__(self,rayon) -> None:
        self.__rayon = rayon

    
    @property
    def rayon(self)->int:
        return self.__rayon

    @rayon.setter
    def rayon(self,rayon:int)->None:
        self.__rayon = rayon

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__rayon=}"