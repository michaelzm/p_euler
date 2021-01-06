prime = False
primenumbers = [3,5]
start_n = 1
counter = 2 
last_prime = 0
dosearch = True
while dosearch:
        prime = True
        if start_n % 2 != 0 and start_n % 3 != 0 and start_n % 5 != 0 and start_n != 1:
                #pn candidate
                for pn in primenumbers:
                        if start_n % pn == 0:
                                prime = False
                        if not prime:
                                break
                if prime:
                        if start_n < 2000000:
                                primenumbers.append(start_n)
                                last_prime = start_n
                                counter += 1
                                if counter % 1000 == 0:
                                        print("found 1000 primenumbers")
                                        print("last found: "+str(last_prime))
                        else:
                                dosearch = False
        start_n += 1            
sum = 2 
for i in primenumbers:
	sum += i	
print(sum)
