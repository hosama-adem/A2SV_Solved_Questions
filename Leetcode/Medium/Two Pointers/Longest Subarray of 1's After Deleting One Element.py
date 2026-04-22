class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # nums_count = Counter(nums)
        
        # if 1 not in nums:
        #     return 0
        # if 0 not in nums:
        #     return nums_count[1]-1

        j = 1
        left = 0
        max_len = 0
        for right in range(len(nums)):
            while j == 0  and nums[right] == 0:
                if nums[left] == 0 :
                    j += 1

                left += 1
            if nums[right] == 0:
                j -= 1
         
            max_len = max(max_len,right-left)
        
        return max_len
            

            
