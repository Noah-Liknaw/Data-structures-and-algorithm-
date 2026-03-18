t = int(input())

while t > 0:
    n = int(input())    
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    i=0
    minOps = []
    while i+3 <= len(nums):
        minOp = (nums[i+1] - nums[i]) + (nums[i+2] - nums[i+1])
        minOps.append(minOp)
        i+=1
    print(min(minOps))
    t-=1