from Rectangle import Rectangle

def main():
    print(Rectangle.get_cpt())
    r = Rectangle(2,5)
    r1 = Rectangle.build_from_str("2,5")
    print(r.get_cpt())
    print(r1)

    
    # r1 = Rectangle(12,85)
    # print(Rectangle.get_cpt())
    # del r
    # print(Rectangle.get_cpt())
    # del r1
    # print(Rectangle.get_cpt())

if __name__ == '__main__':
    main()
