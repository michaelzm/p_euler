prime = False
primenumbers = [3,5]
start_n = 1
counter = 2 
while counter != 10003:
	prime = True
	if start_n % 2 != 0 and start_n % 3 != 0 and start_n % 5 != 0 and start_n != 1:
		#pn candidate
		for pn in primenumbers:
			if start_n % pn == 0:
				prime = False
			if not prime:
				break
		if prime:
			primenumbers.append(start_n)
			counter += 1
	start_n += 1		
print(primenumbers[9999])

