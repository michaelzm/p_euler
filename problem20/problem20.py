def fak(x):
  fak = 1
  for i in range(1, x+1):
    fak *= i
  return fak
number = fak(100)
str_number = str(number)
sum = 0
for c in str_number:
  sum += int(c)
print(sum)
