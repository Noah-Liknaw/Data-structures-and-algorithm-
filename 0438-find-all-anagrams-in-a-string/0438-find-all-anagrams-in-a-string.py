class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sorted_p = sorted(p)
        for i in range(len(s)- len(p) + 1):
            sub = s[i:i+len(p)]
            sub = sorted(sub)
            if(sub == sorted_p):
                ans.append(i)
        return ans