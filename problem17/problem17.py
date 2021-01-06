#1 to 9
def getUnus(n):
	print("getUnus", str(n))
	if n == 0:
		return 0
	if n == 1:
	#o n e
		return 3
	elif n == 2:
	#t w o
		return 3 
	elif n == 3:
	#t h r e e 
		return 5
	elif n == 4:
	#f o u r 
		return 4
	elif n == 5:
	#f i v e
		return 4
	elif n == 6:
	#s i x 
		return 3
	elif n == 7:
	#s e v e n
		return 5
	elif n == 8:
	#e i g h t
		return 5
	elif n == 9:
	#n i n e
		return 4
#10 to 20
def getDecemTil20(n):
	print("getDecemTil20")
	wordcount = 0
	if n == 10:
		return 3
	elif n == 11:
		return 6 
	elif n == 12:
		return 6
	elif n == 13:
		return 8
	elif n == 14:
		return 8
	elif n == 15:
		return 7
	elif n == 16:
		return 7
	elif n == 17:
		return 9
	elif n == 18:
		return 8
	elif n == 19:
		return 8
#teen
def getTeenPostfix():
	print("getTeenPostfix")
	#t e e n
	return 4


def getDecem(n):
	print("getDecem", str(n))
	firstNumber = int(n / 10)
	secondNumber = n % 10
	wordCount = 0
	if n < 10:
		return getUnus(n)
	if firstNumber == 0:
		wordCount += getUnus(secondNumber)
	if firstNumber == 1:
		wordCount = getDecemTil20(n)
	else:
		if firstNumber == 2:
			#t w e n t y
			wordCount +=6
		elif firstNumber == 3:
			#t h i r t y
			wordCount += 6
		elif firstNumber == 4:
			#f o r t y 
			wordCount += 5
		elif firstNumber == 5:
			#f i f t y
			wordCount += 5
		elif firstNumber == 6:
			#s i x t y
			wordCount += 5
		elif firstNumber == 7:
			#s e v e n t y
			wordCount +=7
		elif firstNumber == 8:
			#e i g h t y
			wordCount += 6
		elif firstNumber == 9:
			#n i n e t y
			wordCount +=6
		wordCount += getUnus(secondNumber)
	return wordCount

def getCentum(n):
	centumNumber = int(n / 100)
	decemNumber = n % 100
	wordCount = 0
	print("getCentum",str(centumNumber), str(decemNumber))
	#always add >>hundred<<
	wordCount += 7
	
	#only add >>and<< if decemNumber >0
	if decemNumber > 0:
		wordCount += 3

	wordCount += getUnus(centumNumber)
	wordCount += getDecem(decemNumber)

	return wordCount
def getNumberLetterCount(n):
	if n < 10:
		return getUnus(n)
	elif n < 100:
		return getDecem(n)
	else:
		return getCentum(n)

w_count = 0
for i  in range(1, 1000):
	w_count += getNumberLetterCount(i)	
w_count += 11
print(w_count)

test = getNumberLetterCount(900)
print(test)
#n i n e h u n d r e d 
#18
