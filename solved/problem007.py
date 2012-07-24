#!/usr/bin/env python
# Written by: DGC

print("RUNNING PROBLEM 7")
print("Find the 10001st prime.")
primes = [2]
i = 3
while len(primes) < 10001:
    truth = 1
    for j in primes:
        if (i % j) == 0:
            truth = 0
            break
    if truth == 1:
        primes.append(i)
    i += 1
for it in primes:
    print it
#print(primes[it])



    

