class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i , num in freq.items():
            if num>len(nums)/2:
                return i
        
        

        

        
