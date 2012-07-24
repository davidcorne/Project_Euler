#!/usr/bin/env python
# Written by: DGC
import time
import fileinput
import primes as primes_mod

t_start = time.time()
print("RUNNING PROBLEM 357")
print("Prime generating integers\n")

limit = 10001
#limit = 101
prime_generators = []
primes = primes_mod.primes_bellow(limit)

print("Generating prime generators")
for incr in range(1,limit):
    divisors = []
    prime_divisors = []
    for j in range(1,incr+1):
        if (incr % j == 0):
            # append the crazy formula
            divisors.append(j+(incr/j))
    for p in primes:
        for pos in divisors:
            if (p == pos):
                prime_divisors.append(pos)
    divisors.sort()
    if (divisors == prime_divisors):
        prime_generators.append(incr)
print(prime_generators)
sum = 0
for temp in prime_generators:
    sum += temp
print(sum)
print("run time:"),
print(str(time.time()-t_start))
