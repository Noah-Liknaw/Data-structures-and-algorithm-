class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix= [1] * len(nums)
        i=1
        while i < len(nums):
            prefix[i] = prefix[i-1] * nums[i-1]
            i= i+1
        i= len(nums)-1
        postfix = 1
        while i>=0:
            prefix[i] *= postfix
            postfix*=nums[i]
            i = i-1
        return prefix