class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        
        times = len(piles)//3
        output = 0

        for i in range(1, times*2 , 2):
            output += piles[i]
        
        return output
