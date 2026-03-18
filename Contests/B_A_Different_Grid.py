t = int(input())
while t>0:
    n,m = list(map(int,input().split()))
    a= [ list(map(int,input().split())) for _ in range(n)]
    print(n,m,a)
    
    possible = False
    
    if n == 1 and m == 1:
        print(-1)
    else:
        for r in range(n):
            re= a[r][::-1]
            print(re)
        
    
    

    t-=1


