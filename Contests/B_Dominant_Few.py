t = int(input())

while t>0:
    n = int(input())
    nums = list(map(int,input().split()))
    
    nums = sorted(nums)

    l,r = 1, len(nums)-2
    elite_count = 1
    elite_sum = nums[-1]
    crowd_count=1
    crowd_sum = nums[0]
    possible = False
    while l <= r :

        if crowd_sum  <= elite_sum:
            crowd_sum+=nums[l]
            crowd_count +=1
            l+=1 
        else:
            elite_sum+=nums[r]
            elite_count +=1
            r-=1
            
        if ((elite_sum > crowd_sum ) and elite_count < crowd_count):
            possible = True
            break
    
    print("YES" if possible else "NO")
    t-=1