
import os
from sys import platform
import matplotlib.pyplot as plt
import random
import math

# So what I want to do is to go through the bifork again, going through a first, then going through x. As we go through x however we want to find
# what the final x is and compare them to each other. So I'll need an input of a, and input of x, and to store those x's as a tuple in a dictionary.

# Output = {a: (xf1, xf2, xf3, ... xfN)}


def main():
    root = platformer()
    cwd = os.getcwd()
    # ffig = os.path.join(cwd, 'f_a.png')
    # sfig = os.path.join(cwd, 'sin_a.png')

    a_scale = 10
    x_scale = 100
    dotsize = 0.1
    jumps = 1

    a_max = 4
    a_max_scaled = a_max * a_scale
    a_min_sacled = 1

    x_max = 1
    x_max_scaled = x_max * x_scale
    x_min_scaled = 0
    
    iterations = 1000
    digits = 5

    forks = bifurcations(a_max=a_max_scaled, a_scale=a_scale, digits=digits, x_min=1, x_max=x_max_scaled, x_scale=x_max_scaled, x_iterations=iterations)

    # So now how to find the period numbers? I need to check each a and count how many unique values are in the tuple. Can I do that? Or would it
    # be better to make this a dataframe?

    for a, xs in forks.items():
        print(a)
        for x in xs:
            print(f'\t{x}')


def bifurcations(a_min=1, a_max=40000, jumps=1, a_scale=10000, x_min=0, x_max=10, x_scale=10, x_iterations=100, digits=3):

    forks = {}

    for i in range(a_min, a_max, jumps):
        
        a = i/a_scale

        x = tuple(round(fofa(a, x/x_scale, x_iterations), digits) for x in range(x_min, x_max))

        forks[a] = x

    return forks


def jitter(scale=1):
    sign = random.choice(['+', '-'])

    j = random.random()
    j = j / scale
    j = round(j, 3)

    # if sign in '-':
    #     j = -j

    return j


def fofa(a: float, x: float, n: int):
    for _ in range(n):
        x = a*x*(1-x)

    return x


def sofa(a: float, x: float, n: int):
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
    