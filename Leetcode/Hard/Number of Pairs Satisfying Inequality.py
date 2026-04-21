class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]
        sorted_list = []
        count = 0
        for  val in arr:
            count += bisect_right(sorted_list, val + diff)
            insort (sorted_list, val)
        
        return count 
