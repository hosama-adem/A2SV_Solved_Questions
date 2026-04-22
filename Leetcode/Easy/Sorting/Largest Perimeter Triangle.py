class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        i = len(nums) - 1
        while i > 1:
            if nums[i-2] + nums[i-1] > nums[i]:
                return (nums[i-2] + nums[i-1] + nums[i])
            i -= 1   
        return 0
        



        
