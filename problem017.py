#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 17")
print("How many letters would be needed to write all the numbers in words from 1 to 1000?\n")

def count(num):
    index = len(str(num))
    digits = []
    for i in range(0, index):
        digits.append(int(str(num)[i]))
    if (len(digits) == 1):
        return chars_in(digits[0])
    elif (len(digits) == 2):
        return 3
    elif (len(digits) == 3):
        return 4
    else:
        return 11

def chars_in(num):
    assert(0<= num and num < 10)
    ret = 80
    if (num in [1, 2, 6]):
        ret = 3
    elif (num in [4, 5, 9]):
        ret = 4
    elif (num in [3, 7, 8]):
        ret = 5
    elif (num == 0):
        ret = 0
    else:
        assert(1)
    return ret

total = 0
for i in range(1, 1001):
    print(count(i))
    total += count(i)
print(total)
#print("Letters needed is %i" %(total))

print("\nRun Time:"),
print(str(time.time()-t_start))
