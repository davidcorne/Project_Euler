#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 21")
print("Evaluate the sum of all amicable pairs under 10000.\n")

pairs = []
total = 0
for i in range(1,10000+1):
    divisors = []
    sum = 0
    for j in range(1,i/2+1):
        if (i % j ==0):
            divisors.append(j)
            sum += j
    new_divisors = []
    new_sum = 0
    for k in range(1,sum/2+1):
        if (sum % k ==0):
            new_divisors.append(k)
            new_sum += k
    if (new_sum == i and sum != i):
        pairs.append(i)
        total += i
print("pairs"),
print(pairs)
print("sum")
print(total)
print("run time:"),
print(str(time.time()-t_start))
