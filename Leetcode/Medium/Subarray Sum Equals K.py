class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_arr = 0
        runing_sum = 0
        pre = {0:1}

        for num in nums:
            runing_sum += num
            if (runing_sum-k) in pre:
                sub_arr += pre[runing_sum-k]

            pre[runing_sum] = pre.get(runing_sum,0)+1
        
        return sub_arr
