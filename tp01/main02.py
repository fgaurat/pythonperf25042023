from collections import deque


# HelloWorld : UpperCamelCase, PascalCase => class
# helloWorld : camelCase => method, property
# hello_world : snake_case => var
# hello-world : kebab-case => web

# def add(a,b,c,d,e)
def add(*args): # passage de param positionnel en nombre variable
    print(args)
    r=0
    for value in args:
        r+=value

    return r

def hello(**kwargs):
    print(kwargs)
    print("Hello",kwargs['name'],kwargs['firstName'])
    print("Hello",*kwargs.values())# print("hello",'Fred', 'GAURAT', 'dev', '46')

# def hello2(pos1,pos2,/,pos_or_keyword1,pos_or_keyword2,*,keyword1,keyword2):
# def hello2(name,firstName): # pos or keyword
# def hello2(*,name,firstName):keyword only
def hello2(name,firstName,/): # pos only
    print("Hello2",name,firstName)


def main():
    # hello(firstName="Fred",name="GAURAT",job="dev",age="46")
    hello2(firstName="Fred",name="GAURAT")
    hello2("Fred","GAURAT")


def main02():
    v = [1,2,3,4,5]
    r = add(1,2,3,4,56,12,15)
    print(r) # 15
    r = add(*v) # add(1,2,3,4,5)
    print(r) # 15

    v = [1,2,3,4,5]
    v1 = 1,2,3,4,5
    a,b,c,d,e =v
    print(c)


def main01():
    l = [10,20,30]

    l.append(40)
    print(l)
    l.insert(0,0)
    print(l)
    # list -> stack
    last = l.pop()
    print(l)
    print(last)
    first = l.pop(0)
    print(l)
    print(first)

    d = deque(l)
    d.append(1000)
    print(d)
    print(l)



if __name__ == '__main__':
    main()
