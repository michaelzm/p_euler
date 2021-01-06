primenumbers = [3,5]
#calc 100 prime numbers
start_n = 1
while len(primenumbers) < 10000:
	if start_n % 2 != 0 and start_n % 3 != 0 and start_n % 5 != 0 and start_n != 1:
		#pn candidate
		for pn in primenumbers:
			if start_n % pn == 0:
				#break when its a multiple of known pn
				break
		primenumbers.append(start_n)
		print(start_n)
	start_n += 1

print(primenumbers)

prob = 600851475143
largestpn = 0
goon = True
while goon:
	dobreak = False
	for pn in primenumbers:
		if prob % pn == 0:
			dobreak = True
			print("new prob:"+str(prob))
			prob = prob / pn	 
			print("divided")			
			if pn > largestpn:
				largestpn = pn
			print(largestpn)
	if not dobreak:
		goon = False
print(prob)
print(largestpn)
