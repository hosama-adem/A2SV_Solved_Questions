class Solution:
    def maxScore(self, s: str) -> int:
        count_zeros = max_s = 0
        count_ones = s.count("1")

        for i in range(len(s)-1):
            count_zeros += s[i] == "0"
            count_ones -= s[i] == "1"
            max_s = max(max_s, count_zeros + count_ones)

        return max_s
