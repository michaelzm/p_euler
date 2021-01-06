def rec_chainlength(n, cl):
	if(n>1):
		if n % 2 == 0:
			cl = rec_chainlength(n/2, cl+1)
		else:
			cl = rec_chainlength(n*3+1, cl+1)
	return cl


maxChain = 0
outputStr = ""
for i in range(1, 1000000):
	cl = rec_chainlength(i, 0) 
	if cl > maxChain:
		maxChain = cl
		outputStr = str(maxChain) +", "+ str(i)
print(outputStr)
