t = int(input())

while t > 0:
    n = int(input())
    total = 0
    a = [int (x) for x in input().split()]
    total = sum(a)
    if total%n != 0:
        print(-1)
    else:
        average = total/n
        k=0
        for n in a:
            if average < n:
                k+=1
        print(k)  
    t-=1