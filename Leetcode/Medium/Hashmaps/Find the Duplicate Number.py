class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count = 0
        count = set()

        for num in nums:
            if num in count:
                return num
            count.add(num)
        
        
            
        
