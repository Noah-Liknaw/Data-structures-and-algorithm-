class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sPiles = sorted(piles)
        r = len(piles)-1
        myCoins = []
        for i in range (0,int(len(piles)/3)):
            r -=1
            myCoins.append(sPiles[r])
            r -=1
        
        return sum(myCoins)

        