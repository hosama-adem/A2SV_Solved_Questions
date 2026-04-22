class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        prefix = 0
        result = 0

        for num in nums: 
            prefix += num
            if prefix - goal in count:
                result += count[prefix - goal]
            
            count[prefix] = count.get(prefix,0)+1
        
        print(count)
        return result 
