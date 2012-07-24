#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 12")
print("What is the value of the first triangle number to have over five hundred divisors?")
triangles = []
print_divisors = []
top = 1
while 1:
    temp_sum = 0
    for inc in range(0,top):
        temp_sum += inc
        divisors = []
    triangles.append(temp_sum)
    for number in range(1,triangles[len(triangles)-1]+1):
        if temp_sum % number == 0:
            divisors.append(number)
    print(temp_sum),
    print(len(divisors))
    print_divisors = list(divisors)
    if len(divisors) > 500:
        break
    top += 1
print(print_divisors)
print("The number is:"),
print(print_divisors[len(print_divisors)-1])
print("With"),
print(len(print_divisors)),
print("divisors")
print("run time:"),
print(str(time.time()-t_start))
