class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for i,val in count.items():
            if val == 2:
                res.append(i)
                break

        for i in range(1,len(nums) + 1):
            if count[i] == 0:
                res.append(i)
                break
        
        return res
            
