class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxu = max(nums)
        d = set(nums)
        for i in range(1, maxu):
            if i not in d:
                return i
        
        if maxu + 1 < 1:
            return 1
        return maxu + 1
