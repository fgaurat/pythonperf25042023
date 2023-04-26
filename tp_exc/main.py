import traceback


class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__("Div par 12 hoooooooo !")

def div(a,b):
    if b ==12:
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    r=0
    try:
        print('ouverture fichier')
        r = div(a,b)
    finally:
        print('fermeture fichier')
    
    return r

def main():
    a = 2
    b = 12
    c = call_div(a,b)
    print(c)

def main01():
    try:
        a=2
        b=int(input("b: "))
        c = a/b
        print(c)

    except ZeroDivisionError as e:
        print("erreur !",e)
        traceback.print_exc()
    except TypeError as e:
        print("erreur !",e)
        traceback.print_exc()
    except ValueError as e:
        print("erreur !",e)
        traceback.print_exc()
    except DivBy12Error as e:
        print("DivBy12Error erreur !",e)
        traceback.print_exc()
    except Exception as e:
        print("erreur !",e)
        traceback.print_exc()
    else:
        print("pas d'erreur")
    finally:
        print("finally")    
    
    print("la suite du code")

if __name__ == '__main__':
    main()
