class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums=sorted(nums) 
        if len(nums) > 2:
            return nums[-3]
        else:
            return max(nums) 