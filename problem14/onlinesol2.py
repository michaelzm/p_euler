def CachedFunction(func):
  cache = dict()

  def cached_func(*args):
    if args in cache:
      return cache[args]
    result = func(*args)
    cache[args] = result
    return result
  return cached_func

@CachedFunction
def collatz(N):
	if N == 1: return 1
	if N&1: return 1 + collatz(3*N + 1)
	else: return 1 + collatz(N//2)

lim = 1000000
maxLen = 0
maxN = 0
for i in range(1, lim):
	a = collatz(i)
	if a > maxLen:
		maxLen = a
		maxN = i
print(maxN, maxLen)
