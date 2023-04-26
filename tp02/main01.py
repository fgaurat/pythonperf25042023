
def make_incrementor(inc_value):

    l = list(range(inc_value))

    def inc_function(value):
        l.append(value)
        print(l)
        return value+inc_value
        
    return inc_function





def main():
    inc = make_incrementor(10)
    inc2 = make_incrementor(20)
    v = inc(5)
    print(inc2(5))
    print(v) # 15




if __name__ == '__main__':
    main()
