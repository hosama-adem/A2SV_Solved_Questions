class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        val = list(count.values())
        val.sort()
        max_val = set(val[-k:])
        result = [key  for key , val in count.items() if val in max_val]
        return result
        
