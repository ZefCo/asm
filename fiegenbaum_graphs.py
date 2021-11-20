from typing import Generator
import matplotlib.pyplot as plt
import numpy as np
import os


def fiegen_plots(a:float, n:int, x_values_total: int = 1001):
    x_values: tuple = tuple(x for x in range(x_values_total))
    period: int = 2**n
    # print(x_values, type(x_values))


def logic_iterator(n: int, a: float, x: float = 0.5, fun = None) -> float:
    if fun is None:
        fun = lambda a, x: a*x*(1 - x)

    period: int = 2**n

    for _ in range(period):
        x = fun(a, x)
    
    return x


def multiple_plots():
    a_n_f = [2.0,
             3.23,
             3.4985616,
             3.5546408]
            #  3.5656673]
            #  3.5692435,
            #  3.5697952,
            #  3.5699134]

    a_n_s = [0.5,
             0.77,
             0.82,
             0.84]

    a = a_n_f
    # a = a_n_s

    logic_map: function = lambda a, x: a*x*(1 - x)
    # sin_map: function = lambda a, x: a*np.sin(np.pi * x)

    funny = logic_map

    x_max = 1000

    for n in range(len(a)):
        x_gen = (x for x in range(x_max + 1))

        plot_values = {x/x_max:logic_iterator(n, a[n], x=x/x_max, fun=funny) for x in x_gen}
        output_file = os.path.join(os.getcwd(), f'a{n}_{a[n]}.png')
    
        plt.plot(plot_values.keys(), plot_values.values())
        plt.plot(plot_values.keys(), plot_values.keys())
        plt.xlabel('inital x values')
        plt.ylabel('final x values')
        plt.title(f'Logic Map: f = a*sin(pi*x)\na{n} = {a[n]}\nusing N={x_max} points')
        plt.savefig(output_file)
        plt.close()

    # plt.savefig(f'All logic maps overlain')
    # plt.show()


        # print(a_n_f[n])


def flip(n, on = False):
    if on:
        if (n % 2) == 0:
            f = 1
        else:
            f = -1

    else:
        f = 1

    return f


def main():
    '''
    Include a y=x line, then find where the y=x line intersects the other iterators. That is the point that you want to zoom in on.
    NOT where the slope of the iterator is zero, but where it intersects at y=x
    '''

    # multiple_plots()

    a_n_f = [2.0,
             3.23606797749979,
             3.4985616,
             3.5546408,
             3.566667379856268,
             3.5692435,
             3.5697952,
             3.5699134]

    logic_map: function = lambda a, x: a*x*(1 - x)
    sin_map: function = lambda a, x: a*np.sin(np.pi * x)

    funny = logic_map
    # funny = sin_map

    n: int = 4
    # switch = False
    # x_max_float: float = 0.69
    # x_min_float: float = 0.5 - (x_max_float - 0.5)
    x_min_float: float = 0.4887
    x_max_float: float = 0.5 + (0.5 - x_min_float)
    x_scale: int = 10000
    # x_max_float: int = 1
    # x_min_float: int = 0
    a: float = a_n_f[n]
    # flip = 1
    # s = flip(n)
    switch = False if ((n % 2) == 0) else True
    s: int = flip(n, on=switch)
    scaler: int = 1 if switch else 0
    # scaler = 0
    # print(s)

    x_min = int(x_min_float*x_scale)
    x_max = int(x_max_float*x_scale)
    # x_gen = (x for x in range(x_max + 1))
    x_gen: Generator = tuple(x for x in range(x_min, x_max + 1))
    print(len(x_gen))

    plot_values: dict = {x/x_scale:(s*logic_iterator(n, a, x=x/x_scale, fun=funny) + scaler) for x in x_gen}

    output_file: str = os.path.join(os.getcwd(), 'f_plots', f'a{n}_{a}.png')
    
    plt.plot(plot_values.keys(), plot_values.values())
    plt.plot(plot_values.keys(), plot_values.keys())
    plt.xlabel('inital x values')
    plt.ylabel('final x values')
    plt.title(f'Logic Map: f = a*x*(1-x)\na{n} = {a}')
    # plt.axis('off')
    # plt.savefig(output_file)
    plt.show()



if __name__ in '__main__':
    main()
