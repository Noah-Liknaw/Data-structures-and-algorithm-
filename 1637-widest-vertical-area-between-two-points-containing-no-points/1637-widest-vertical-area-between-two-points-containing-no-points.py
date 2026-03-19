class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [i[0] for i in points]
        x.sort()
        max_len = 0
        for i in range(len(x)-1):
            max_len = max(max_len,(x[i+1]-x[i]))
        return max_len

