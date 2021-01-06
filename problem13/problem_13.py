problem = open('problem_txt.txt', 'r')
numbers = []
for line in problem:
	numbers.append(int(line))
sum = 0
for n in numbers:
	sum += n

print(sum)	
sum_str = str(sum)
result = ""
counter = 0
for c in sum_str:
	if counter < 10:
		result += c
		counter += 1
print(result)
