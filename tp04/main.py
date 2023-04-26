from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo

def show_surface(o:ICalcGeo):
    print("show_surface")
    print(o.surface)

def main():
    ce = Cercle(5)
    print(ce.surface)


def main01():
    c = Carre(2)
    print(c.surface)
    print(c)
    c.cote = 5
    print(c.surface)
    print(c)
    print(50*'-')
    ce = Cercle(5)
    print(ce.surface)

    show_surface(c)
    show_surface(ce)

if __name__ == '__main__':
    main()
