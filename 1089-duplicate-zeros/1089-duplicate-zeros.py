from collections import deque 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        q = deque()

        for i in range(len(arr)):
            q.append(arr[i])
            if arr[i] == 0:
                q.append(0)

            arr[i] = q.popleft()

