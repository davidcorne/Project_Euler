#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 039")
print("If p is the perimeter of a right angle triangle, {a, b, c}, which value, for p <= 1000, has the most solutions?\n")

perimeters = []

for m in range(1,31):
    for n in range(1,m):
        tri = [m**2 - n**2, 2*m*n, m**2 + n**2]
        k = 1
        while (k*tri[0] + k*tri[1] + k*tri[2] <= 1000):
            tri = [k*tri[0], k*tri[1], k*tri[2]]
            perimeters.append(k*tri[0] + k*tri[1] + k*tri[2])
            k +=1
print("run time:"),
print(str(time.time()-t_start))
