class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # piles.sort()
        
        while l <= r:
            mid = l + (r-l) // 2
            h_spent = 0
            for pile in piles:
                h_spent += math.ceil(pile / mid)
            if h_spent <= h:
                r = mid - 1
                # ans = mid
            else:
                l = mid + 1
        return l