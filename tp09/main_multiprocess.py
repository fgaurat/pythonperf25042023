import os
import time
from multiprocessing import Pool

def f(x):
    return x*x

def main():
    print(os.cpu_count())
    
    with Pool() as p:
        print(p.map(f, [1, 2, 3]))


if __name__ == '__main__':
    main()
