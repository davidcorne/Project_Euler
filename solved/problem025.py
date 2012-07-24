#!/usr/bin/env python
# Written by: DGC
import time
t_start = time.time()

print("RUNNING PROBLEM 25")
print("What is the first term in the Fibonacci sequence to contain 1000 digits?")

fibonacci = [1,1]
i = 2
while (1):
	fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
	if (len(str(fibonacci[i-1])) == 1000):
		string = str(fibonacci[i])
#		for j in range(1,len(fibonacci)):
#			print(j),
#			print(fibonacci[j-1]),
#			print(len(str(fibonacci[j-1])))
		print(len(fibonacci)-1)
		break
	i += 1
print("run time:"),
print(str(time.time()-t_start))
