class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple = 2
        while(multiple %n  != 0):
            multiple+=2
        return multiple