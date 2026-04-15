class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtracking(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            backtracking(i + 1, subset)
            subset.pop()
            backtracking(i + 1, subset)
        
        nums.sort()
        backtracking(0, [])
        res = [list(subset) for subset in res]

        return res
