#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 30")
print("Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.\n")
# 999999 > 6*9^5 = 354294 so only need to check to 1000000

total = 0
limit = 1000000
for i in range(2,limit):
    as_string = str(i)
    quintic_sum = 0
    for j in range(0,len(as_string)):
        quintic_sum += int(as_string[j]) ** 5
    if (quintic_sum == i):
        total += quintic_sum
print(total)
print("run time:"),
print(str(time.time()-t_start))
