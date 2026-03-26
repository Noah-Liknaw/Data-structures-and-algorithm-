t = int(input())
while t>0:
    n = int(input())
    s = input()
    l,r = 0,len(s)-1
    result= "Yes"
    flip = True
    while l<r:
        while l<r and s[l]!=s[r] and flip:
            l+=1
            r-=1
            if s[l]==s[r]:
                flip =False
        if s[l]!=s[r]:
            result="No"
        l+=1
        r-=1
    print(result)
    t-=1