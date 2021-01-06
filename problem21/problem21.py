overallSum = 0
def getDivisors(n):
  result = 0
  for i in range(1,int(n/2+1)):
    if n % i == 0:
      print(i)
      result += i
  return result
printstmt = getDivisors(220)
print(printstmt)

def calcMatch(n):
  global overallSum
  outputFirst = getDivisors(n)
  outputSecond = getDivisors(outputFirst)
  if outputSecond != outputFirst:
    if n == outputSecond:
      print(n)
      print("match")
      overallSum += n
    else:
      print("no match")
for i in range(1,10000):
  calcMatch(i)
calcMatch(223)
print(overallSum)
