firstLine= list(map(int,input().split()))
nSize= firstLine[0]
mSize = firstLine[1]

n = list(map(int,input().split()))
m = list(map(int,input().split()))


l,r = 0,0
answer = []

while r < mSize:
    counter = 0
    while l < nSize and n[l] < m[r]:
        counter+=1
        l+=1
    answer.append(counter)    
    r+=1
 
print(answer)