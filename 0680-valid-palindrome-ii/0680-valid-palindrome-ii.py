class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                l1, r1 = l + 1, r
                l2, r2 = l, r - 1

                while l1 < r1 and s[l1] == s[r1]:
                    l1 += 1
                    r1 -= 1

                while l2 < r2 and s[l2] == s[r2]: 
                    l2 += 1
                    r2 -= 1

                return l1 >= r1 or l2 >= r2  

            l += 1
            r -= 1

        return True

    