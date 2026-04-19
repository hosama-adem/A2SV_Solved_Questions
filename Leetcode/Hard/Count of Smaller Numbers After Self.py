class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = []
        res = []

        for num in reversed(nums):
            pos = bisect_left(sorted_list, num)
            res.append(pos)
            sorted_list.insert(pos, num)
        
        return res[::-1]
