class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n

        #buliding freq
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        # prefix sum
        for i in range(1, n):
            freq[i] += freq[i - 1]

        # sort both
        nums.sort()
        freq.sort()

        # compute result
        MOD = 10**9 + 7
        res = 0
        for i in range(n):
            res = (res + nums[i] * freq[i]) % MOD

        return res
