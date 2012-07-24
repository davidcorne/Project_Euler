#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()
print("RUNNING PROBLEM 36")
print("Find the sum of all numbers less than one million, which are palindromic in base 10 and base 2.\n")
# find palindromes

sum = 0
for i in range (1,1000000+1):
    num = str(i)
    reverse = num[::-1]
    truth = 1
    for j in range(0,len(num)):
        if (num[j] != reverse[j]):
            truth = 0
            break
    if (truth == 1):
        num_b = ""
        for inc in range(2,len(bin(i))):
            num_b += bin(i)[inc]
            reverse_b = num_b[::-1]
            truth_b = 1
            for k in range(0,len(num_b)):
                if (num_b[k] != reverse_b[k]):
                    truth_b = 0
                    break
        if (truth_b == 1):
            sum += i
print("Sum is:"),
print(sum)
print("run time:"),
print(str(time.time()-t_start))
