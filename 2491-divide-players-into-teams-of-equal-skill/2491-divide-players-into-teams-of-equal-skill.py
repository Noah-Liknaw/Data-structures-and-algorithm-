class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        
        total = sum(skill)
        teams = n // 2
        
        if total % teams != 0:
            return -1
        
        target = total // teams
        chemistry = 0
        
        l, r = 0, n - 1
        
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        
        return chemistry