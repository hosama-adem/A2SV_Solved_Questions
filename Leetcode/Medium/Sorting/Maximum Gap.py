class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        gaps = []
        for i in range(len(nums) - 1):
            gaps.append(nums[i + 1] - nums[i])
        
        return max(gaps)
