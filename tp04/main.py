from Rectangle import Rectangle
from Carre import Carre

def main():
    c = Carre(2)
    print(c.surface)
    print(c)
    c.cote = 5
    print(c.surface)
    print(c)


if __name__ == '__main__':
    main()
