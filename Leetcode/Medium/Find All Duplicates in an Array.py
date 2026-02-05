class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        res = set()

        for i in nums:
           freq[i] = freq.get(i,0)+1
        for key ,value in freq.items():
            if value == 2 :
                res.add(key)
        
        return list(res)
                    
