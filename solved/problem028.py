#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 28")
print("What is the sum of both diagonals in a 1001 by 1001 spiral?\n")

size = 1001
incr = 2
sum = 1
test = 1
last = 1
count = 1
for i in range(3,size*size+1):
    if (i == last + incr):
        if (count == 4):
            count = 0
            incr += 2
        last = i
        sum += i
        count += 1
print("sum is"),
print(sum)
print("run time:"),
print(str(time.time()-t_start))
