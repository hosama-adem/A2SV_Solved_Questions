class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        odd = n // 2
        mod = 10**9 + 7

        return (pow(5, even, mod) * pow(4, odd, mod)) % mod
