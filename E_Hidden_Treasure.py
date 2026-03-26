n,m = list(map(int,input().split()))
l,r = 1,n
while m >0:
    s = input().split()
    if s[2] == "left":
        l = min(r,int(s[4]))
    else:
        r = max(l,int(s[4]))
    m-=1

res = -1
if l > r and l < n and r>= 0:
    res = l-r-1

print(res)
