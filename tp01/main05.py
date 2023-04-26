# def get_value(i):
#     return i

def main():
    a=2
    l = []

    for i in range(10):
        l.append(i)

    print(l)
    l = list(map(lambda i:i,range(5,20,3)))

    print(l)
    
    l = [i**2 for i in range(10) if i%2] # Comprehension list , liste en intention. Pythonic way
    print(l)



if __name__ == '__main__':
    main()
