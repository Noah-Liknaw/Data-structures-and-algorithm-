class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        num_mismatch = 0
        fc = []
        sc = []
        for c1,c2 in zip(s1,s2):
            
            if c1 != c2:
                fc.append(c1)
                sc.append(c2)
                num_mismatch +=1
                if num_mismatch > 2:
                    return False

        if num_mismatch == 0:
            return True
        if num_mismatch == 2:
            return fc[0] == sc[1] and fc[1] == sc[0]
        
        return False
