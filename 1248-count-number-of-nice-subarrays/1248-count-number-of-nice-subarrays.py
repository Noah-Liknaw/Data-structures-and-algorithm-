class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            res = 0
            
            for right in range(len(nums)):
                if nums[right] % 2:
                    k -= 1
                    
                while k < 0:
                    if nums[left] % 2:
                        k += 1
                    left += 1
                    
                res += right - left + 1
                
            return res
        
        return atMost(k) - atMost(k-1)