from collections import Counter 
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        aCount = Counter(a)
        bCount = Counter(b)
        return aCount == bCount
        