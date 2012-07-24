#!/usr/bin/env python
# Written by: DGC
import time
import fileinput
t_start = time.time()
print("RUNNING PROBLEM 49")
print("Find arithmetic sequences, made of prime terms, whose four digits are permutations of each other.\n")

# get prime numbers between 1000 and 9999
primes = []
for line in fileinput.input("/c/Users/dgc/Dropbox/Coding/primes.txt"):
    temp_prime = int(float(line))
    if (temp_prime > 20000):
        break
    if (temp_prime > 1000):
        primes.append(temp_prime)
perm_triples = []
for p in primes:
    for i in primes[primes.index(p)+1:len(primes)]:
        if (primes.count(p+2*(i-p)) != 0):
            one_s = str(p)
            two_s = str(i)
            three_s = str(p+2*(i-p))
            one = []
            two = []
            three = []
            for inc in range(0,4):
                one.append(one_s[inc])
                two.append(two_s[inc])
                three.append(three_s[inc])
            one.sort
            two.sort
            three.sort
            print one, two, three
            if (one == two and two == three):
                perm_triples.append([p,i,p+2*(i-p)])
print(perm_triples)
print("run time:"),
print(str(time.time()-t_start))
