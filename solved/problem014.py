#!/usr/bin/env python
# Written by: DGC
# Algorithm:
#   if even n :-> n/2
#   if odd  n :-> 3n+1

import time
t_start = time.time()
print("RUNNING PROBLEM 14")
print("Find the longest sequence using a starting number under one million.\n")
all = []

for i in range(1,1000000+1):
    current = i
    sequence = []
    while (current != 1):
        if (current % 2 == 0):
            current = current / 2
        else:
            current = 3*current + 1
        sequence.append(current)
    all.append([len(sequence),i])
print (max(all)[1])
print("run time:"),
print(str(time.time()-t_start))
