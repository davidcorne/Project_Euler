#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 40")
print("Finding the nth digit of the fractional part of the irrational number.\n")

numbers = ""
i = 1
while (1):
    numbers = numbers + str(i)
    if (len(numbers) > 1000001):
        break
    i += 1
product = 1
for j in [1,10,100,1000,10000,100000,1000000]:
    product *= int(float(numbers[j-1]))
print(product)
print("run time:"),
print(str(time.time()-t_start))
