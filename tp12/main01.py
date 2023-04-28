import numpy as np
import pandas as pd


def main():
    x = np.arange(15, dtype=np.int64).reshape(3, 5)
    print(x)
    data = pd.read_csv('./MOCK_DATA.csv')
    print(data)

if __name__ == '__main__':
    main()
