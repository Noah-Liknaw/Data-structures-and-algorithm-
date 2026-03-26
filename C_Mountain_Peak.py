t = int(input())

while t >0:
    n = int(input())
    h = list(map(int,input().split()))
    h.sort()
    i=0
    j=1
    k=2
    result = False
    while k < len(h):
        if h[i] < h[j] and h[j] > h[k]:
            result = True
            print("YES")
            print(i,j,k)
            break
        i+=1
        j+=1
        k+=1
    
    if not result:
        print("NO")
    t-=1