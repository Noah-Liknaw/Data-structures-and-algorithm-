class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = -1
        for num in nums2:
            print(i)
            nums1[i] = num
            i-=1
        
        return nums1.sort()
        