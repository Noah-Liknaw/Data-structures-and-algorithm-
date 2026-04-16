class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(curn,curk):
            if curn == 1:
                return 0
            half = curn//2

            if curk > half:
                return 1-helper(curn//2,curk-half)
            elif curk <=half:
                return helper(curn//2,curk)    
        return helper((2**(n-1)), k)                