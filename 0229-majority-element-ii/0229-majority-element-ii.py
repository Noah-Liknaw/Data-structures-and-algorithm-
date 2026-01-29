from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = []
        freq = Counter(nums)
        for key,value in freq.items():
            if value > n//3:
                results.append(key)
        return results