t = int(input())
while t > 0:
    n = int(input())
    if n == 2:
        print(2)
    elif n == 3:
        print(3)
        
    else:
        ng = -1
        ngThree = -1
        ngTwo = -1
        while n >= -2:
            n = n - 3 
            if n >= 1:
                ngThree+=1
            else:
                ngTwo+=1
            ng += 1
        print(ng,ngTwo,ngThree)
    
    t-=1