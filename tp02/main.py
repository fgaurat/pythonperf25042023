
def do_log(p=""):
    def wrapper_main(func):
        def wrapper(*values, **kwargs):
            print("LOG", p, values)
            r = func(*values, **kwargs)
            print("LOG", p, r)
            return r

        return wrapper
    return wrapper_main


@do_log("a")
@do_log("b")
def say_hello(name):

    return f"hello {name}"


def main():
    h = say_hello("fred")
    print(h)


if __name__ == '__main__':
    main()
