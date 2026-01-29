from collections import Counter

class Solution:
    def isSubset(self, a, b):
        freqa = Counter(a)
        freqb = Counter(b)

        for key, value in freqb.items():
            if key not in freqa or value > freqa[key]:
                return False

        return True
