class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for i in counts:
            if counts[i]>1:
                return True
        return False
        
