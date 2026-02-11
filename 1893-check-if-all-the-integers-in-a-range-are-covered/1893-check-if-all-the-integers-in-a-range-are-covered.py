class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = [0] * 52
        for start, end in ranges:
            nums[start] += 1
            nums[end + 1] -= 1

        for i in range(1,52):
            nums[i] += nums[i-1]

        for i in range(left,right+1):
            if nums[i] <= 0:
                return False

        return True 