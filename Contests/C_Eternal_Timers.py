t = int(input())
while t >0:
    n = int(input())
    a = []
    a = [int(x) for x in input().split()]
    if min(a) == 1:
        print("NO")
    elif len(a) == 1:
        print("YES")
    elif(len(a) == 2):
        if a[0] == a[1]:
            print("NO")
        else:
            print("YES")
    else:
        lenToR  = a.index(a[-1]) - a.index(min(a))
        lenToL = a.index(min(a)) 
        maxD = max(lenToL, lenToR)
    
        if min(a)-1 >= 2*maxD :
            print("YES")
        else:
            print("NO") 

    
    t-=1