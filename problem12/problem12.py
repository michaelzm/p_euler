import time
import digits
divisors = 1
#save the number of divisors for each number
arr_nums = [] 
holder_divisors = []
start_t = time.time()
it_counter = 0
wh_1_counter = 0
wh_2_counter = 0
natural_num = 1
highest_num = 1
hBase = 0
while divisors < 50:
	number_time_s = time.time()
	arr_nums = []
	#add 2 (one for 1 divisor, one for highest_num divisor)
	mod_count = 2 
	natural_num += 1
	highest_num += natural_num
	print(" ***************************** check num: "+str(highest_num))
	print("add the number itself to mod_count")
	holder_divisors = [highest_num, 1]
	c_div_op = 2
	ongoing = True
	while ongoing:
		n_to_p = highest_num	
		addable = False
		print("check")
		print(n_to_p, c_div_op)
		while n_to_p % c_div_op == 0:
			print("now divider: "+str(c_div_op))
			it_counter += 1
			wh_1_counter += 1
			if not c_div_op in holder_divisors:
				print("adding to dividers: "+str(c_div_op))
				holder_divisors.append(int(c_div_op))
				print(holder_divisors)
			print(str(n_to_p)+ " dividable by "+str(c_div_op))
			n_to_p /= c_div_op
			print("adding the result "+str(n_to_p))
			if not n_to_p in holder_divisors:
				print("adding "+str(n_to_p)+" to known divisors")
				holder_divisors.append(int(n_to_p))
			mod_count += 1
			print("current divisors count: "+str(len(holder_divisors)))
			print(holder_divisors)
			addable = True

		#get the next number to check
		foundNextDiv = False
		while not foundNextDiv:
			c_div_op += 1
			if c_div_op < 11: 
				foundNextDiv = True
			else:
				print(str(c_div_op)+" now too large")
				ongoing = False
				foundNextDiv = True 
	if len(holder_divisors) > divisors:
		divisors = len(holder_divisors)		
	print("NEW HIGHEST FOUND= div: "+str(divisors)+" num: "+str(highest_num))
	print(sorted(holder_divisors))

end_t = time.time()
print(end_t - start_t)
print(it_counter)
print("wh1, wh2")
print(wh_1_counter, wh_2_counter)
# 36 
# 2 -> 18, 9, 2
# 3 -> 12, 4, 3
# 4
# 5
# 60 -> 2,3,4,5,6,  7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
# 60 -> 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60
# 2= 30, 15
# 3= 20
# 4= 15
# 5= 12
# 6= 10 
# 7= x
# 8= x
# 9= x
# 10=6
# 11=x
# 12=x
# 13x
# 14x
# 15x
#
#
#
#

