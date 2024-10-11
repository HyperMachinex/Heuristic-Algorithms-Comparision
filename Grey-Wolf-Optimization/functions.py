import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum

function = "sum(x**2)"

def createFunction(f):
    function = f

def custom(x):
    x = np.asarray_chkfinite(x)
    return eval(function)

def selectFunction(cbIndex):
        switcher = {
        0: ackley,
        1: dixonprice,
        2: griewank,
        3: perm,
        4: rastrigin,
        5: rosenbrock,
        6: schwefel,
        7: sphere,
        8: zakharov,
    }
        return switcher.get(cbIndex, "nothing")

def ackley( x, a=20, b=0.2, c=2*pi ):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    n = len(x)
    s1 = sum( x**2 )
    s2 = sum( cos( c * x ))
    return -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)

#...............................................................................
def dixonprice( x ):  # dp.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 2, n+1 )
    x2 = 2 * x**2
    return sum( j * (x2[1:] - x[:-1]) **2 ) + (x[0] - 1) **2

#...............................................................................
def griewank( x, fr=4000 ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    s = sum( x**2 )
    p = prod( cos( x / sqrt(j) ))
    return s/fr - p + 1

#...............................................................................
def perm( x, b=.5 ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    xbyj = np.fabs(x) / j
    return mean([ mean( (j**k + b) * (xbyj ** k - 1) ) **2
            for k in j/n ])
    # original overflows at n=100 --
    # return sum([ sum( (j**k + b) * ((x / j) ** k - 1) ) **2
    #       for k in j ])

#...............................................................................
def rastrigin( x ):  # rast.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 10*n + sum( x**2 - 10 * cos( 2 * pi * x ))

#...............................................................................
def rosenbrock( x ):  # rosen.m
    """ http://en.wikipedia.org/wiki/Rosenbrock_function """
        # a sum of squares, so LevMar (scipy.optimize.leastsq) is pretty good
    x = np.asarray_chkfinite(x)
    x0 = x[:-1]
    x1 = x[1:]
    return (sum( (1 - x0) **2 )
        + 100 * sum( (x1 - x0**2) **2 ))

#...............................................................................
def schwefel( x ):  # schw.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 418.9829*n - sum( x * sin( sqrt( abs( x ))))

#...............................................................................
def sphere( x ):
    x = np.asarray_chkfinite(x)
    return sum( x**2 )

#...............................................................................
def zakharov( x ):  # zakh.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    s2 = sum( j * x ) / 2
    return sum( x**2 ) + s2**2 + s2**4
