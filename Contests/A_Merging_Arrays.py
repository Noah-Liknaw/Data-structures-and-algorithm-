firstLine = list(map(int,input().split()))
nSize = firstLine[0]
mSize = firstLine[1]


n = list(map(int,input().split()))
m = list(map(int,input().split()))


l,r = 0,0
print(nSize,mSize)
answer = []
while l < nSize and r < mSize:
    if n[l] < m[r]:
        answer.append(n[l])
        l+=1
    else:
        answer.append(m[r])
        r+=1
    print(l ,r)

while l < nSize:
    answer.append(n[l])
    l += 1

while r < mSize:
    answer.append(m[r])
    r += 1


print(answer)
