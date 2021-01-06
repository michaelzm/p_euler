#3x3 = 6 token = 6bit
#3x 1, 3x0

#20x20 = 40 token = 40 bit

#permutation:

def getFak(n):
	fak = 1
	for i in range(1,n+1):
		print(i)
		fak *=i

	return fak		

top = getFak(40)
bottom = getFak(20)

result = top / (bottom * bottom)
print(result)
