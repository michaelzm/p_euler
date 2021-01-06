n1 = 0
n2 = 0

largestpal = 0

for i in range(1, 999):
	for j in range(1,999):
		ph = i*j
		print(ph)
		#now mirror number
		ph_str = str(ph)
		ph_str_2 = ""
		for k in reversed(range(len(ph_str))):
			ph_str_2 += ph_str[k]
		if ph == int(ph_str_2):
			if ph > largestpal:
				largestpal = ph
print(largestpal)
