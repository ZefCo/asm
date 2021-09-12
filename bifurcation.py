
import os
from sys import platform
import matplotlib.pyplot as plt
import random
import math


def main():
    root = platformer()
    cwd = os.getcwd()
    ffig = os.path.join(cwd, 'f_a.png')
    sfig = os.path.join(cwd, 'sin_a.png')

    scale = 10000
    dotsize = 0.1
    jumps = 1

    amax = 4 * scale
    amin = 1
    
    aaxis = []
    faxis = []
    saxis = []
    for i in range(amin, amax, jumps):
        iters = 100
        
        a = i/scale
        aaxis.append(a)

        x: float = jitter()

        f: float = fofa(a, x, iters)
        faxis.append(f)

        s: float = sofa(a, x, iters)
        saxis.append(s)
    
    plt.scatter(aaxis, faxis, s=dotsize)
    plt.xlabel('a')
    plt.title('f(x) = a x (1-x)')
    plt.savefig(ffig)

    plt.close()

    plt.scatter(aaxis, saxis, s=dotsize)
    plt.xlabel('a')
    plt.title('f(x) = a sin(pi x)')
    plt.show(sfig)


def jitter(scale=1):
    sign = random.choice(['+', '-'])

    j = random.random()
    j = j / scale
    j = round(j, 3)

    # if sign in '-':
    #     j = -j

    return j


def fofa(a: float, x0: float, n: int):
    x = x0
    for _ in range(n):
        x = a*x*(1-x)

    return x


def sofa(a: float, x0: float, n: int):
    x = x0
    for _ in range(n):
        x = a*math.sin(math.pi * x)

    return x


def platformer():
    user: str = 'ethanspeakman'
    if platform == 'linux' or platform == 'linux2':
        home: str = os.path.join('/', 'home', user)

        return home

    elif platform == 'win32':
        cdrive: str = os.path.join('C:/')
        ddrive: str = os.path.join('D:/')

        return ddrive

if __name__ in '__main__':
    main()
    