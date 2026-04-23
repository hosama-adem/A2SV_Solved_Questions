class Solution:
    def longestNiceSubstring(self, s: str) -> str:  
        if len(s) < 2:
            return ""    
            
        letters = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in letters:
                left_side = self.longestNiceSubstring(s[:i])
                right_side = self.longestNiceSubstring(s[i+1:])

                return left_side if len(left_side) >= len(right_side) else right_side 
            
        return s
        
