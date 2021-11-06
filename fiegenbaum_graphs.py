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
             3.5546408,
             3.5656673,
             3.5692435,
             3.5697952,
             3.5699134]

    a_n_s = [0.5,
             0.77,
             0.82,
             0.84]

    logic_map: function = lambda a, x: a*x*(1 - x)
    sin_map: function = lambda a, x: a*np.sin(np.pi * x)

    funny = sin_map

    x_max = 10000000

    for n in range(len(a_n_f)):
    # for n in range(4):
        x_gen = (x for x in range(x_max + 1))

        plot_values = {x/x_max:logic_iterator(n, a_n_s[n], x=x/x_max, fun=funny) for x in x_gen}
        output_file = os.path.join(os.getcwd(), f'a{n}_{a_n_s[n]}.png')
    
        plt.scatter(plot_values.keys(), plot_values.values(), s=1)
        plt.xlabel('inital x values')
        plt.ylabel('final x values')
        plt.title(f'Logic Map: f = a*sin(pi*x)\na{n} = {a_n_s[n]}\nusing N={x_max} points')
        plt.savefig(output_file)
        plt.close()

    # plt.savefig(f'All logic maps overlain')


        # print(a_n_f[n])


def main():

    multiple_plots()

    # a_n_f = [2.0,
    #          3.23,
    #          3.4985616,
    #          3.5546408,
    #          3.5656673,
    #          3.5692435,
    #          3.5697952,
    #          3.5699134]

    # logic_map: function = lambda a, x: a*x*(1 - x)
    # sin_map: function = lambda a, x: a*np.sin(np.pi * x)

    # funny = logic_map
    # # funny = sin_map
    # n = 0
    # a = a_n_f[n]

    # x_max = 1000
    # x_gen = (x for x in range(x_max + 1))

    # plot_values = {x/x_max:logic_iterator(n, a, x=x/x_max, fun=funny) for x in x_gen}

    # # print(plot_values)

    # output_file = os.path.join(os.getcwd(), f'a{n}_{a}.png')
    
    # plt.scatter(plot_values.keys(), plot_values.values(), s=5)
    # plt.xlabel('inital x values')
    # plt.ylabel('final x values')
    # plt.title(f'Logic Map: f = a*x*(1-x)\na{n} = {a}')
    # # plt.show()
    # plt.savefig(output_file)


if __name__ in '__main__':
    main()