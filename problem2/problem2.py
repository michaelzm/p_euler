fib1 = 1
fib2 = 2

sumfib = 2
while fib1 < 4000000:
	nextfib = fib1+fib2
	if nextfib % 2 == 0:
		sumfib += nextfib
	fib1 = fib2
	fib2 = nextfib
print(sumfib)
