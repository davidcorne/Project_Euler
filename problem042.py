#!/usr/bin/env python
# Written by: DGC
import fileinput
import time
t_start = time.time()
print("RUNNING PROBLEM 42")
print("How many triangle words does the list of common English words contain?\n")

# the text file has words of maximum length 14 (17 with "", included
# found by running cat Data/words.txt | sed -e 's/,/,\n/g' | awk '{ print length(), $0 | "sort -n" }' in shell
# this means we only need triangle numbers up to 14*9 = 126
triangle = []
n = 1
while (1):
    current = n*(n+1)/2
    if (current > 126):
        break
    triangle.append(current)
    n += 1
number = 0
for line in fileinput.input("temp.txt"):
    line_total = 0
    final_index = line.index["\n"]
    line = line[0:final_index]
    for char in line:
        num_char = ord(char)-64
        # the ascii of \n
#        if (num_char != -54):
        line_total += num_char

    if (line_total in triangle):
        number += 1
        print(line_total),
        print(line)
print(number)
print(triangle)
print("run time:"),
print(str(time.time()-t_start))
