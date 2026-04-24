class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
         houses.sort()
         heaters.sort()
        
         res = 0
        
         for house in houses:
             i = bisect.bisect_left(heaters, house)
            
             left_dist = float('inf') if i == 0 else house - heaters[i-1]
             right_dist = float('inf') if i == len(heaters) else heaters[i] - house
            
             closest = min(left_dist, right_dist)
             res = max(res, closest)
        
         return res