#!/usr/bin/env python
# Written by: DGC
import time
import math

t_start = time.time()
print("RUNNING PROBLEM 356\n")

def cbrt(x):
    from math import pow
    if x >= 0: 
        return pow(x, 1.0/3.0)
    else:
        return -pow(abs(x), 1.0/3.0)

def polar(x, y, deg=0):         # radian if deg=0; degree if deg=1
    from math import hypot, atan2, pi
    if deg:
        return hypot(x, y), 180.0 * atan2(y, x) / pi
    else:
        return hypot(x, y), atan2(y, x)

def quadratic(a, b, c=None):
    import math, cmath
    if c:               # (ax^2 + bx + c = 0)
        a, b = b / float(a), c / float(a)
    t = a / 2.0
    r = t**2 - b
    if r >= 0:          # real roots
        y1 = math.sqrt(r)
    else:               # complex roots
        y1 = cmath.sqrt(r)
    y2 = -y1
    return y1 - t, y2 - t

def cubic(a, b, c, d=None):
    from math import cos
    if d:                       # (ax^3 + bx^2 + cx + d = 0)
        a, b, c = b / float(a), c / float(a), d / float(a)
    t = a / 3.0
    p, q = b - 3 * t**2, c - b * t + 2 * t**3
    u, v = quadratic(q, -(p/3.0)**3)
    if type(u) == type(0j):     # complex cubic root
        r, w = polar(u.real, u.imag)
        y1 = 2 * cbrt(r) * cos(w / 3.0)
    else:                       # real root
        y1 = cbrt(u) + cbrt(v)
    y2, y3 = quadratic(y1, p + y1**2)
    ret = max(y1 - t, y2 - t, y3 - t)
    return ret

sum = 0
for i in range(1,31):
    sum += cubic(1,-(2**i),0,i)**987654321

print(sum)
print("run time:"),
print(str(time.time()-t_start))
