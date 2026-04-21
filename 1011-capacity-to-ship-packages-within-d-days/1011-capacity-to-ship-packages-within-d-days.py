class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = -1

        def canShip(cap):
            days_used = 1
            curW = 0
            for w in weights:
                if curW +w > cap:
                    days_used +=1
                    curW=0
                curW+=w
            return days_used <= days

        while low <= high:
            cap = low + (high -low) // 2

            if canShip(cap):
                ans = cap
                high = cap-1
            else:
                low = cap + 1
        
        return ans