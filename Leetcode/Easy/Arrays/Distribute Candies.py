class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans = min(len(set(candyType)), len(candyType)//2)
        return ans
