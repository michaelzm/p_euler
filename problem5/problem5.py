solution = False
pass_ = True
num = 1 
nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
while not solution:	
	pass_ = True
	for i in nums:
		if not num % i == 0:
			num+=1
			pass_ = False
			break
	if pass_:	
		solution = True
print(num)
