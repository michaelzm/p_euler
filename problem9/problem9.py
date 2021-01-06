#a + b + c = 1000
#a<b<c
#3e2 + 4e2 = 9 + 16 = 25 = 5e2
#a*a + b*b = c*c

#looking for abc

#1+2+997 = 1000
#increment b and c until b == c
#then increment a and repeat incrementing b and c until matching sum parts
#then save sum parts
ongoing = True
goal = 1000

result = ""
result_num = 0
for a in range(1000):
	for b in range (a, 1000):
		if b > a: 
			c = 1000 - a - b
			if c > b and b > a:
				print(a,b,c)
				if a*a + b*b == c*c:
					print("found")	
					print(a, b, c)
					result_num = a*b*c
					result = str(a)+str(b)+str(c)
print(result)
print(result_num)
