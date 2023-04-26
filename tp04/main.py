from Rectangle import Rectangle
from data_class import Rectangle as RectangleData
def main():
    r = Rectangle(12,5)

    print(r.longueur)
    r.longueur = 12
    print(r.longueur)

    # print(r._Rectangle__longueur)
    print(r.longueur) # 12
    assert r.longueur == 12

    print(r.largeur) # 5
    assert r.largeur == 5

    print("surface",r.surface)
    print(50*'-')
    r2 = RectangleData(5,16)
    print(r2.largeur)
    print(r2.longueur)
    print(r2)
    print(50*'-')
    
    s= str(r)
    print(s)
    print(50*'-')

    r1 = Rectangle(5,6)
    r2 = Rectangle(5,6)

    # if r1.__eq__(r2):
    if r1 == r2:
        print('ok')
    else:
        print('ko')


if __name__ == '__main__':
    main()
