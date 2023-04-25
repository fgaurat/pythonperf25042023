

a = 2

def main(): #  hoisting
    global a
    print("main",a)
    a=3
    print("main",a)

if __name__ == '__main__':
    main()



print("end",a) 