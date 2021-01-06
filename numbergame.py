import time
start = time.time()
found = False 
number = 10
for i in range(0,3000000):
	#start with number 10
	#we need to swap first and last digit

	#convert number to string
	num_str = str(number)


	#swap chars

	num_str_ph = num_str

	last_i = len(num_str) - 1

	num_str_2 = num_str
	num_empty = ""
	num_empty += num_str_ph[last_i]
	for char in range(0, last_i):
		num_empty += num_str_ph[char]


	second_number = int(num_empty)

	if number * 2 == second_number:
		print("works for num: "+num_str_ph)
		found = True
	else:
		number += 1
end = time.time()
print(end-start)
