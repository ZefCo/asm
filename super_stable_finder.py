
def newt(a: (float or int), 
        x0: (float or int), 
        threshold: float = 10**-10, 
        dx0: (float or int) = 1, 
        delta: (float or int) = 1, 
        n_period: (float or int) = 1, 
        e: float = 10**-7,
        safety=10**5):
    '''
    This checks for a super stable point. Then it preforms a functional call to find the 
    height at that value of a (here called displacement)
    '''

    if abs(delta) < threshold:
        print(f"Method fails: delta = {delta} < threshold = {threshold} before calculations. Please enter delta such that delta > threshold")

    else:

        period = 2**n_period
        i = 0

        # fNext = lambda a, f: a*f*(1 - f)
        # dfNext = lambda a, f, daf: f*(1 - f) + a*(1 - 2*f)*daf

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

        print(f'############\nn = {n_period}\na = {a}\n$ $ $')

        displace = peak(a, x0, period)

        print(f'$ $ $\ndispalce = {displace}\n############')

        # while abs(x) > threshold:
        #     x = f(a, x)


def peak(a, x0, period):
    x = x0

    for _ in range(1, int(period / 2)):
        x = f(a, x)

    displace = x - x0

    return displace


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


def a_predicts(a: (float or int), a_p: (float or int), d = 4.66):

    a_new = a + (a - a_p)/d

    return a_new


def main():
    '''
    This does nothing more then execute the code. It is composed of function calls.
    '''
    a0: float = 3.3
    x0: float = 0.5
    n_period: int = 1
    threshold: float = 10**-13
    safety: float = 10**8
    e: float = 10**-7
    # e = 1

    newt(a0, x0, n_period=n_period, safety=safety, e=e, threshold=threshold)

def test():
    f = 0.5
    a = 3.5

    fNext = lambda x, y: x*y*(1 - y)
    dfNext = lambda a, f, daf: f*(1 - f) + a*(1 - 2*f)*daf

    f_1 = fNext

    f_2 = fNext(a, f)
    f_3 = f_1(a, f)

    print(f'f_1 = {f_1}')
    print(f'f_2 = {f_2}')
    print(f'f_3 = {f_3}')



# def fNext(a, f):
#     y = a * f * (1 - f)

#     return y


if __name__ in '__main__':
    main()

    # test()