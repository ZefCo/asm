# import math
# from operator import xor
import numpy as np
# import sympy as sp
import auto_diff as ad
import autograd as ag
import random

from numpy.lib.arraysetops import isin


def test_pass(f, x0, *args, **kwargs):
    print(kwargs, type(kwargs))

    x = x0

    for _ in range(10):

        x = f(x, *args, **kwargs)
        print(f'####\n\tx={x}\n\t{kwargs}, {type(kwargs)}\n$$$$')

    # return y


def newt(f, x0, 
         threshold=10**-13, 
         max_steps=1000, 
         nudge=10**-3, 
         target=0, 
         sigma=None,
         *args,
         **kwargs):
    '''
    Newton's method in Python. Finds the roots of an input fuction. The function needs to be defined as another method, as this requiers the use of autograd to compute the derivative.

    Sigma is a piece factor that allows a bit more fine tuning. If set to None Sigma is taken as 1 and the whole piece of f(x)/f'(x) is used.
    '''

    # print(kwargs, type(kwargs))
    # print(**kwargs)
    # this is inputing a dictionary, so how to I get the dictionary later?

    if isinstance(x0, int):
        x0 = float(x0)

    x = x0
    fprime = ag.grad(f)

    rootnotfound = True

    i = 0
    
    while rootnotfound:
        print(x, kwargs, type(kwargs))

        y = f(x, *args, **kwargs)
        # print(y)

        if y < (target + threshold) and y > (target - threshold):
            rootnotfound = False
            print(f'\nFinished\nTook {i} steps to complete')

            return x

        else:

            if fprime(x) == 0:
                print("Stopping: f'(x) = 0, divide by zero error")
                rootnotfound = False

            else:
                b = y / fprime(x)

                if sigma is None:
                    a = 1
                else:
                    a = sigma / (sigma + abs(b))
                
                x = x - (a * b)
                i += 1

        if i > max_steps:
            rootnotfound = False
            print(f'Reached max number of steps, y={y}')

            return x
    # pass


def sin(x, *args, n: int = 10, **kwargs):

    if n < 0:
        return None
    
    elif n == 0:
        return x    
    else:
        nn = (2*n) + 1
        return (((-1)**n)/factorial(nn)) * (x**nn) + sin(x, n=n-1)


def cos(x, *args, n: int = 10, **kwargs):

    if n < 0:
        return None
    
    elif n == 0:
        return 1
    
    else:
        nn = (2*n)
        return (((-1)**n)/factorial(nn)) * (x**nn) + cos(x, n=n-1)


def x_squared(x, *args, **kwargs):

    y = x**2

    return y


def x_cubed(x, *args, **kwargs):

    y = x**3 + 2*x**2 +2

    return y


def f_a(a, n=1):

    if n == 1:
        return (1/4)*a

    else:
        return f_a(a, n=n-1)


def x_poly(x: float, *args, coefficents: (list or tuple or np.array) = None, **kwargs):
    '''
    Because the other one is not working in conjunction with Newton's Method (for some reason they just blow up to the far ends, never getting close to the actual root), this is an
    attempt to just strip it down and get it working. Also this doesn't work so... fuck.

    For some reason doing the polynomial as a straight up method (as in manually putting in the polynomial) works just fine with newt(), so I don't know what's wrong with this.
    '''
    if coefficents is None:
        y = x**2

        return y

    else:
        if isinstance(coefficents, (list, tuple)):
            coefficents: np.array = np.transpose(np.array(coefficents))

        highest_order = len(coefficents)

        powers = [(highest_order - power) for power in range(1, highest_order + 1)]

        x_array = [x**power for power in powers]

        y = np.matmul(coefficents, x_array)

        return y


def x_poly_old(x: float, *args, coefficents: (list or tuple or np.array) = None, powers: (list or tuple or np.array) = None, zeroth_term: int = 0, **kwargs):
    '''
    By default this will calculate y = x**2 just by putting in a value for x.

    WARNING: Order matters for any inputs.

    You can also input an array of coefficents, or an array of powers and an array of coefficents (dictioanry support comming later).
    -If an array of coefficents only, it will take the length of the coefficents and create a powers array of the same length starting at the highest power and stopping at 0.
    For this reason the order of coefficents matters, along with place holders of 0. It would interpret a vector of [1, 2, 3, 4] as having powers [3, 2, 1, 0]. If you skip a
    0 you will get a lower order polynomial then intended.
    -If an array or coefficents and polynomials are input then it will raise x to each of those powers, then use matrix multiplication to find the value. These arrays must be
    the same length, else the code will fail.
    
    It will also add a zeroth term, always. The zeroth term is 0 by default, so a power of 0 can be input manually and the coefficent can be set as 0. However it is recomended
    to use c*x**0 whenever possible. 
    '''

    # print('#### In x_poly function ####')
    # print(coefficents, type(coefficents))

    if (powers is None) and (coefficents is None):
        y = x**2 + zeroth_term

        # print('#### CONDITION 1 ####')
        # print('#### Exiting x_poly function ####')
        return y

    elif isinstance(coefficents, (list, tuple, np.array)) and (powers is None):

        if isinstance(coefficents, (list, tuple)):
            coefficents: np.array = np.transpose(np.array(coefficents))

        highest_order = len(coefficents)
        powers = [(highest_order - power) for power in range(1, highest_order + 1)]

        x_array = [x**power for power in powers]

        y = np.matmul(coefficents, x_array) + zeroth_term

        # print('#### CONDITION 2 ####')
        # print('#### Exiting x_poly function ####')
        return y
    
    elif isinstance(powers, (list, tuple, np.array)) and isinstance(coefficents, (list, tuple, np.array)):
        
        if isinstance(powers, (list, tuple)):
            powers: np.array = np.array(powers)
        if isinstance(coefficents, (list, tuple)):
            coefficents: np.array = np.transpose(np.array(coefficents))
        
        if len(powers) == len(coefficents):

            x_array = [x**power for power in powers]

            y = np.matmul(coefficents, x_array) + zeroth_term
        
            # print('#### CONDITION 3 ####')
            # print('#### Exiting x_poly function ####')
            return y

        else:
            print(f"Powers and Coefficents must be same length: powers length = {len(powers)}, coefficents length = {len(coefficents)}")    


def factorial(x):
    
    if x < 1:
        return None
    
    elif x == 1:
        return x
    
    else:
        return x * factorial(x - 1)


def jitter_int():
    
    n = random.randint(0, 1)
    
    return n


def percent_error(m, t):
    
    pe = ((m - t)/t) * 100

    return abs(pe)


def percent_diff(m, t):
    
    ave = 0.5 * (m + t)
    pd = ((m - t)/ave) * 100

    return pd


def poly_test():
    x = .4
    in_func = x_poly

    c = [1, -1, -1, 1]

    y = test_pass(in_func, x, coefficents=c)

    print(y, type(y))


def main():
    # input function
    # pick a point at random
    # evaluate function at random point
    # evaluate it's derivative at random point
    # combine
    # repeat

    initial_x = -2.4
    target = -0.5 * np.pi

    # in_func = sin
    in_func = cos
    # in_func = x_squared
    # in_func = x_poly
    # in_func = x_cubed

    c = [1, 2, 0, 2]
    p = [3, 2, 1, 0]

    something_stupid = {'coefficents':c, 'powers':p}

    max_steps = 100

    # sigma = None
    sigma = 10**-2
    # sigma = 1

    print(f'initial point: x0={initial_x}\nfudge factor: sigma={sigma}')

    x = newt(in_func, initial_x, max_steps=max_steps, sigma=sigma, coefficents=c)

    row_hash = '#######'
    for _ in range(len(str(x))):
        row_hash = row_hash + '#'

    print(f"\n{row_hash}\n\nRoot = {x}\n\n{row_hash}")

    print(f'\n\n####\npercent difference = {percent_diff(x, target)}\npercent error = {percent_error(x, target)}\n####')


if __name__ in '__main__':
    main()
    # poly_test()