#!/usr/bin/env python
# Written by: DGC
import time
import fileinput
t_start = time.time()
print("RUNNING PROBLEM 27")
print("Find a quadratic formula that produces the maximum number of primes for consecutive values of n.\n")

# n^2 +an + b
# b must be prime


# get prime numbers
primes = []
highest = 0
values = []
for line in fileinput.input("../primes.txt"):
    temp_prime = int(float(line))
    if (temp_prime > 10000):
        break
    primes.append(temp_prime)

#for a in range(-999,1000):
for a in range(-9,10):
    for b in primes:
        values = [[a,b]]
        if (b > 10):
            break
        # don't need to check n = 0 as b is prime
        n = 1
        result = 0
        while (1):
            result = n**2 + a*n + b
            print(result),
            values.append(result)
            if (not (result in primes)):
                if (n > highest):
                    highest = n
                    values = [a,b]
                print(values),
                print((result in primes))
                break
#print(highest),
#print(values)
print("run time:"),
print(str(time.time()-t_start))
