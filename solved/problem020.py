#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 20")
print("Find the sum of digits in 100!")

fact = 1
for i in range(1,101):
	fact *= i
list_of_ints = [int(j) for j in str(fact)]
sum = 0
for k in range(0,len(list_of_ints)):
	sum += list_of_ints[k]
print(sum)
print("run time:"),
print(str(time.time()-t_start))

