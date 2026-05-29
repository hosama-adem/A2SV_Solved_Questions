class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        sl = list(s)
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            if left < right:
                sl[left], sl[right] = sl[right], sl[left]
                left += 1
                right -= 1

        print(sl)
        return "".join(sl)
