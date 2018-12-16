import numpy as np
from matplotlib import pyplot as plt


def f(x):
    """最小値を求めたい関数"""
    return x ** 2


def df(x):
    """最小値を求めたい関数の一階導関数"""
    return 2 * x


def main():
    x = np.arange(-2, 2, 0.1)

    y = f(x)
    plt.plot(x, y, label='f(x)')

    y_dash = df(x)
    # 一階導関数の符号を反転させる
    plt.plot(x, -y_dash, label='-f\'(x)')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
