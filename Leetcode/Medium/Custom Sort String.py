class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        freq = Counter(s)
        
        for ch in order :
            if ch  in s:
                res += ch * freq[ch]
                freq[ch] = 0
            
        for i,val in freq.items():
            if val > 0:
                res += i*val
            
        return res
