
import os
from sys import platform
import matplotlib
import sympy
from sympy.matrices import Matrix
from sympy import exp
import numpy as np
import pandas
import math
# from math import exp
import scipy
from matplotlib import pyplot as plt


def main():
    # root = platformer()
    # problem1()
    # pass
    problem4()


def problem1():
    cwd = os.getcwd()
    dim = 10**-3
    time = [.1, .24, .38, .52, .66, .8, .94, 1.08, 1.22, 1.36, 1.50, 1.65, 1.79, 1.93, 3.26, 3.53, 3.80, 4.07, 4.34, 4.61, 15.0, 25.0, 34.0, 53.0, 62.0]
    time[:] = [t*dim for t in time] 
    radius = [11.1, 19.9, 25.4, 28.8, 31.9, 34.2, 36.3, 38.9, 41.0, 42.8, 44.4, 46.0, 46.9, 48.7, 59.0, 61.1, 62.9, 64.3, 65.6, 67.3, 106.5, 130.0, 145.0, 175.0, 185.0]
    constant = 550
    radius_the = [(constant * (t**(2/5))) for t in time]
    plt.plot(time, radius, label='Photo Values')
    plt.plot(time, radius_the, label=f'DA Values, C={constant}')
    plt.legend()
    plt.ylabel('Radius [m]')
    plt.xlabel('Time [ms]')

    # plt.show()
    plt.savefig(os.path.join(cwd, 'BombDA.png'))

    # radius_plot = 
    # pass


def problem4():
    h, k = sympy.symbols('h k')
    t: Matrix = Matrix([[exp(-h + k), exp(-k)], [exp(-k), exp(h + k)]])
    # tt = sympy.trace(t)
    # tt = sympy.simplify(tt)
    # print('\n\n', tt, '\n')
    evalues = t.eigenvals()
    evectors = t.eigenvects()
    print(evalues)
    print(evectors)

    # t2 = t * t
    # t2 = sympy.trace(t2)
    # t2 = sympy.simplify(t2)
    # print('\n', t2, '\n')
    # t3 = t2 * t
    # t3 = sympy.trace(t3)
    # t3 = sympy.simplify(t3)
    # print('\n', t3, '\n')
    # t4 = t3 * t
    # t4 = sympy.trace(t4)
    # t4 = sympy.simplify(t4)
    # print('\n', t4, '\n')


def problem2():
    pass
        

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
    