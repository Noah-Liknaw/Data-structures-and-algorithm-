t = int(input())
while t>0:
    n = int(input())
    nums = list(map(int,input().split()))
    x = int(input())
    if len(nums) == 1:
        print(nums[0] == x)
    nums = sorted(nums)
    if nums[0] < x and nums[-1] > x:
        print("YES")
    else:
        print("NO")
    t-=1