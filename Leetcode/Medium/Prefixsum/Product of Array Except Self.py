class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = 1
        for num in nums:
            d *= num
        if nums.count(0) > 1:
            return [0]*len(nums)

        if nums.count(0) == 1:
            d = 1
            for num in nums:
                if num != 0:
                    d *= num
            s = [0]*len(nums)
            j = nums.index(0)
            s[j] = d
            return s
        for i in range(len(nums)):
            nums[i] = d//nums[i]
        
        return nums
