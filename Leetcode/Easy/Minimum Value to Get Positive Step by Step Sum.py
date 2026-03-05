class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = [0] + nums
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        

        if min(pre) < 0:
            return abs(min(pre))+1
        if pre.count(1) >=1:
            return pre.count(1)
        if pre.count(0)>=1:
            return pre.count(0)
            
        return 1
        
