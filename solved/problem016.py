#!/usr/bin/env python
# Written by: DGC

print("RUNNING PROBLEM 16")
print("What is the sum of the digits of the number 2^1000?")
large = 1
for i in  range(1,1001):
	large *= 2
	print(i),
	print(large)
list_of_ints = [int(j) for j in str(large)]
sum = 0
for k in range(0,len(list_of_ints)):
	print(list_of_ints[k])
	sum += list_of_ints[k]
print(sum)