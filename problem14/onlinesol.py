ls = dict()

for i in range(2,1000000):

    k,l = str(i),1
    
    while i != 1:

        if i%2 == 0:
            i = int(i/2)
            l+=1

        elif i%2 != 0:
            i = 3*i+1
            l+=1
    
    ls[k] = l

lc = max(ls,key=ls.get)
print(lc)
