t = int(input())
while t>0:
    n = int(input())
    a  = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    l = r =0
    op =0
    while l <len(a) and r <len(b):
        if a[l] > b[r]:
            op+=1
            r+=1
        else:
            r+=1
            l+=1
    
    print(op)

    t-=1