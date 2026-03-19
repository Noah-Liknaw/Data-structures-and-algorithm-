class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        itIs = True
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                itIs = False
            l+=1
            r-=1
        
        return itIs