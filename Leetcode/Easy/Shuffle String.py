class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(len(indices)):
                if i == indices[j]:
                    res += s[j]
        return res 
        
