#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 48")
print("Find the last ten digits of 1^1 + 2^2 + ... + 1000^1000.\n")

digits = 0
for i in range(1,1000+1):
    digits += (pow(i,i) % 10000000000)
print(digits % 10000000000)


print("run time:"),
print(str(time.time()-t_start))
