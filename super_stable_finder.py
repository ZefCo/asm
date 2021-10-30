
def newt(a: (float or int), 
        x0: (float or int), 
        threshold: float = 10**-10, 
        dx0: (float or int) = 1, 
        delta: (float or int) = 1, 
        n_period: (float or int) = 1, 
        e: float = 10**-7,
        safety=10**5):
    '''
    This is not working yet. For some reason it just iterates until I tell it to stop.
    '''

    if abs(delta) < threshold:
        print(f"Method fails: delta = {delta} < threshold = {threshold} before calculations. Please enter delta such that delta > threshold")

    else:

        period = 2**n_period
        i = 0

        while abs(delta) > threshold:
            x = x0
            dx = dx0
            
            for _ in range(period):
                
                xx = f(a, x)
                dxx = df(a, x, dx)
                x = xx
                dx = dxx

            delta = (x - x0)/ dx
            
            a = a - (e / (e + abs(delta))) * delta

            i += 1
            if i > safety:
                print(f'Breaking, i is greater then safety, i={i}')
                break

        print(f'############\nn = {n_period}\na = {a}\n############')

        # while abs(x) > threshold:
        #     x = f(a, x)


def f(a: float, x: float):
    '''
    Function f. Written as f(a, x) = a*x(1-x), it returns f(x), here written as x.
    '''
    x = a*x*(1 - x)

    return x


def df(a: float, x: float, dx: float) -> float:
    '''
    The derivative of f. Written as f(a, x) = x(1-x) + a(1-2x)dx.

    It requries an input of a, x, and dx however.

    Returns df
    '''
    dx = x*(1 - x) + a*(1 - 2*x)*dx

    return dx


def main():
    '''
    This does nothing more then execute the code. It is composed of function calls.
    '''
    a0 = 3.5
    x0 = 0.5
    n_period = 2
    threshold = 10**-13
    safety = 10**8
    e = 10**-7
    # e = 1

    newt(a0, x0, n_period=n_period, safety=safety, e=e, threshold=threshold)


if __name__ in '__main__':
    main()