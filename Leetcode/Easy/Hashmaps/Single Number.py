class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for I in nums:
            if nums.count(I)==1:
                return I
                break
