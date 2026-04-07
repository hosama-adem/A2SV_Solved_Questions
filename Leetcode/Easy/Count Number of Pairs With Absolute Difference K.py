class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        pairs = 0

        for i,val in freq.items():
            if i + k in freq:
                pairs += freq[i] * freq[i+k]

        # print(pairs)
        return pairs
        
