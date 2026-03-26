t =  int(input())
while t>0:
    s = input().strip()
    l = 0
    res = set()
    while l < len(s):
        if l+1 <len(s) and s[l] == s[l+1]:
            l+=2
        else:
            res.add(s[l])
            l+=1

    print(''.join(sorted(res)))            
            
    t-=1