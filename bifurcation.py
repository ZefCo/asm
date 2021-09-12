
import os
from sys import platform
import matplotlib.pyplot as plt
import random
import math


def main():
    cwd = os.getcwd()

    func1 = fofa
    a1: int = 4
    path1 = os.path.join(cwd, 'f_fig.png')

    func2 = sofa
    a2: int = 1
    path2 = os.path.join(cwd, 'sin_fig.png')
    
    bifur(a1, func1, close=False)
    bifur(a1, func1, close=False)
    bifur(a1, func1, close=False)
    bifur(a1, func1, close=False)
    bifur(a1, func1, close=False)
    bifur(a1, func1, path=path1)

    bifur(a2, func2, close=False)
    bifur(a2, func2, close=False)
    bifur(a2, func2, close=False)
    bifur(a2, func2, close=False)
    bifur(a2, func2, close=False)
    bifur(a2, func2, path=path2)


def bifur(amax: int, 
          func, 
          scale=10000, 
          dotsize=0.1, 
          jumps=1, 
          path=None,
          show=False,
          close=True):
    '''
    Requires a maximum value for a (pick a to be normalized beforehand), and
    an input fucntion (func). Outputs a bifurcation plot of the input function.
    X is assumed to be normalized and will be chosen at random from between
    0 and 1 using random.random()

    The plot will be saved to a file path if the filepath is input as a string,
    else the plot will be shown for manual saving later.
    '''
    cwd = os.getcwd()
    fig = os.path.join(cwd, 'f_a.png')

    amax: int = amax * scale
    amin: int = 1
    
    aaxis: list = []
    faxis: list = []
    for i in range(amin, amax, jumps):
        iters: int = 100
        
        a: float = i/scale
        aaxis.append(a)

        x: float = jitter()

        f, title = func(a, x, iters)
        faxis.append(f)
    
    plt.scatter(aaxis, faxis, s=dotsize)
    plt.xlabel('a')
    plt.title(title)
    plt.savefig(fig)

    if isinstance(path, str):
        plt.savefig(path)
    
    if show:
        plt.show()

    if close:
        plt.close()


def jitter(scale=1):
    j: float = random.random()
    j: float = j / scale
    j: float = round(j, 3)

    return j


def fofa(a: float, x0: float, n: int):
    x: float = x0
    title: str = 'f(x) = a x (1 - x)'
    for _ in range(n):
        x = a*x*(1-x)

    return x, title


def sofa(a: float, x0: float, n: int):
    x: float = x0
    title: str = 'f(x) = a sin(pi x)'
    for _ in range(n):
        x = a*math.sin(math.pi * x)

    return x, title


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
    