class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_len = 1
        nums = set(nums)

        if len(nums)==0:
            return 0

        for num in nums:

            length = 1
            if num-1 in nums:
                continue
            else:
                while num+1 in nums:
                    length +=1
                    num +=1
            
            all_len = max(all_len,length)

        return all_len
