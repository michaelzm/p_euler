sum_squares = 0
square_sum = 0
for i in range(1,101):
	sum_squares+= i*i
	square_sum += i
square_sum = square_sum*square_sum

print(square_sum - sum_squares)
