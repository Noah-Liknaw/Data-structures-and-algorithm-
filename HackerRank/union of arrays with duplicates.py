class Solution:    
    def findUnion(self, a, b):
        # code here
        union = list(set (a) | set (b))
        return union
            
            