from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = Counter()
        left = 0
        size = 0
        maxf = 0

        for i in range(len(s)):
            letters[s[i]] += 1
            maxf = max(maxf, letters[s[i]])
            all = i - left + 1

            while all - maxf > k:
                letters[s[left]] -= 1
                left += 1
                all = i - left + 1

            size = max(size, all)

        return size
