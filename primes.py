#!/usr/bin/env python
# Written by: DGC

import math
import time

# methods to call importing this
def primes_bellow(limit):
    """Return a list of primes bellow the input argument."""
    primes = [2]
    i = 3
    while i <= limit:
        prime = 1
        for j in primes:
            if (j > math.sqrt(i)):
                break
            if (i % j) == 0:
                prime = 0
                break
        if (prime == 1):
            primes.append(i)
        i += 1    
    return primes

def primes_number_of(limit):
    """Returns the number  of primes bellow the input argument."""
    primes = [2]
    i = 3
    while len(primes) < limit:
        prime = 1
        for j in primes:
            if (j > math.sqrt(i)):
                break
            if (i % j) == 0:
                prime = 0
                break
        if prime == 1:
            primes.append(i)
        i += 1
    return primes

# if this is run as a program.
if __name__ == "__main__":
    type = 3
    while (type != 0 and type != 1):
        type = input("Do you want number of primes [0] or primes below a number [1]?\n")
    limit = 1
    if (type == 0):
        limit = input("How many primes do you want?\n")
    else:
        limit = input("Primes (inclusivly) below what number?\n")
    
    t_start = time.time()
    if (type == 0):
        primes = primes_number_of(limit)
        end_calc = time.time()
        msg = ""
        if (limit < 1000):
            msg = "The first " + str(limit) + " primes are:\n" + str(primes) + "\n"
        msg += "The " + str(limit) + "th primes is: " + str(primes[-1])
        print(msg)
    else:
        primes = primes_bellow(limit)
        end_calc = time.time()
        msg = ""
        if (limit < 1000):
            msg = "The primes bellow " + str(limit) + " are:\n" + str(primes) + "\n"
        msg += "There are " + str(len(primes)) + " primes bellow " + str(limit)
        msg += "\nThe largest of which is: " + str(primes[-1])
        print(msg)
    print("Calculation time:"),
    print(str(end_calc-t_start))
