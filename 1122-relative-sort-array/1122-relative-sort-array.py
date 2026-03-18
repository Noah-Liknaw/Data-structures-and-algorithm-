class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        for x in arr2:
            result.extend([x] * count[x])
            del count[x]

        for x in sorted(count):
            result.extend([x] * count[x])

        return result