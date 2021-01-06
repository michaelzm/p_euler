import digits
import time
start = time.time()
found = False 
number = 10
checked = 0
currentBase = 0;
for i in range(0,100000000):
#while not found:	
	num_base = number // 10
	
	new_num_first_digit = number % 10

	base = digits.getBase(number)
	old_num_first_digit = number // base 
	
	#print(new_num_first_digit, old_num_first_digit)
		
	#for progress, output base
	if base > currentBase:
		currentBase = base
		print("new base: "+str(currentBase))
	if new_num_first_digit == old_num_first_digit * 2 and old_num_first_digit < 5:
		checked += 1 
		new_num_first_digit *= base
		
		num_new_int = new_num_first_digit + num_base
		if number * 2 == num_new_int:
			print("works for num: ")
			print(num_new_int)
			found = True
	number += 1


#   6005 -> 5600
#   6003 -> 3600	 
#   9006 -> 6900
#   306  -> 630


print("checked: "+str(checked))
end = time.time()
print(end - start)

#divtime:0.4973268508911133
#multime:1.1306886672973633
#modtime:0.49264979362487793
