def getdivs(n):
    divs = 1
    c = 0
    d = 2
    while d <= n:
        c = 0
        while n % d == 0:
            c += 1
            n //= d
        divs *= c + 1
        if d == 2:
            d = 3
        else:
            d += 2
    return divs


i = 500
divs = 0
while divs <= 500:
    i += 1
    n = i * (i + 1) // 2
    divs = getdivs(n)
print(i, n, divs)
