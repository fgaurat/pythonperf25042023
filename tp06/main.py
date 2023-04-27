from Rectangle import Rectangle

def main():
    r = Rectangle(1,2)
    r1 = Rectangle(11,22)
    print(hex(id(r)))
    print(hex(id(r1)))
    print(r)
    print(r1)
    r.longueur=1000
    print(r)
    print(r1)
    print(type(r))
    print(type(Rectangle))

if __name__ == '__main__':
    main()
