import sys
import copy
def main():
    a = 10
    print(hex(id(a)))
    l = [10,20,30,40,50,60,70,80,90]
    print(hex(id(l[0])))
    print(hex(id(10)))
    l[0] = 1000
    l1 = l
    l[0] = 59
    print(l) 
    print(l1) 
    l1 = l.copy()
    l[0] = 412
    print(l) 
    print(l1) 
    s = l[3:]
    s = l[:6]
    s = l[:] # l.copy()
    print(s)
    l[0] =10
    print(l)
    print(s)
    # shallow -> superficielle, surface
    print(50*'-')
    
    a = [10,20,30]
    b = [40,50,60]
    c = [70,80,90]
    l = [a,b,c]
    l2 = l[:] # l.copy()
    l2 = copy.deepcopy(l)
    l[1][-1] = 1000
    print(l)
    print(l2)


def main01():
    a = 2 # a  int => inférence de type
    print(sys.getrefcount(2))
    a1 = 2
    print(sys.getrefcount(2))
    a2=a1
    print(sys.getrefcount(2))



    # b = "Toto" # str
    # c = 2.3 # float
    # d = True # False

    # print("a",hex(id(a)))
    # print("a1",hex(id(a1)))
    # a = 3
    # del a
    # print(hex(id(a)))


if __name__ == '__main__':
    main()
