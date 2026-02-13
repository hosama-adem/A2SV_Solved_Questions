class Solution:
   def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant = max(freq, key=freq.get)
        total = freq[dominant]

        prefix_count = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num == dominant:
                prefix_count += 1
            suffix_count = total - prefix_count

            if prefix_count > (i + 1) // 2 and suffix_count > (n - i - 1) // 2:
                return i
        return -1

    
