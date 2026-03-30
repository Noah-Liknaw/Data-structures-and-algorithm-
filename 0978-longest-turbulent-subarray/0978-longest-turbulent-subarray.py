class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        res = 1

        for right in range(1, n):
            c = (arr[right] > arr[right-1]) - (arr[right] < arr[right-1])

            if c == 0:
                left = right
            elif right == n-1 or c * ((arr[right+1] > arr[right]) - (arr[right+1] < arr[right])) != -1:
                res = max(res, right - left + 1)
                left = right

        return res