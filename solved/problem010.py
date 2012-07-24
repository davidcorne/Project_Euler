#!/usr/bin/env python
# Written by: DGC

print("RUNNING PROBLEM 10")
print("Calculate the sum of all the primes below two million.")
primes = [2]
i = 3
while primes[len(primes)-1] < 2000000:
    truth = 1
    for j in primes:
        if (i % j) == 0:
            truth = 0
            break
    if truth == 1:
        primes.append(i)
    i += 1
print(primes)
sum = 0
for it in range(0,len(primes)-1):
    sum += primes[it]
print(sum)


    

