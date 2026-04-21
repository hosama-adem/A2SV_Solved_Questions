class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_arr = []
        cost = 0
        MOD = 10 ** 9 + 7

        for num in instructions:
            smaller = bisect_left(sorted_arr, num)
            greater = len(sorted_arr) - bisect_right(sorted_arr, num)
            cost = (cost+ min(smaller, greater)) % MOD
            sorted_arr.insert(smaller, num)

        return cost


