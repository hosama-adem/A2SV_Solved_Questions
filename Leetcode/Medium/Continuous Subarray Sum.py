class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k == 0:
            return True
        sub = 0
        pre = {0:1}
        
        for i in range(len(nums)):
            sub += nums[i]
            sub %= k

            if sub in pre:
                if pre[sub] > 1:
                    return True
            
            else:
                pre[sub] = nums[i]
            
        return False
