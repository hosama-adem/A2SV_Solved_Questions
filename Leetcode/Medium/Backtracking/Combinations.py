from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        com = []

        def backtrack(ind, comb):
            if len(comb) == k:
                com.append(comb[:])
                return
            
            if ind == len(arr):
                return
            
            
            comb.append(arr[ind])
            backtrack(ind + 1, comb)
            comb.pop()
            
            
            backtrack(ind + 1, comb)

        backtrack(0, [])
        return com
