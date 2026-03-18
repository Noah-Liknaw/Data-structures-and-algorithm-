import random
big = random.randint(1000, 10 ** 6)
t = int(input())

while t > 0:
    n,k = list(map(int,input().split())) 
    bcAdded = {}
    i=0
    while i < k:
        b,c = map(int,input().split())
        if b^big not in bcAdded:
            bcAdded[b^big]=0
        bcAdded[b^big] += c 
        i+=1
    sumsBc = list(bcAdded.values())
    sumsBc.sort()
    totalSum = 0
    i = len(sumsBc)-1
    while n>0 and i >= 0:
        totalSum +=sumsBc[i]
        i-=1
        n-=1

    
    print(totalSum)
    t-=1