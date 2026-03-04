from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        
        for char, count in freq.items():
            buckets[count].append(char)
        
        result = []
        for count in range(len(s), 0, -1):
            for char in buckets[count]:
                result.append(char * count)
        
        return "".join(result)