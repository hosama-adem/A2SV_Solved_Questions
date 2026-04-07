class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter(s[:len(p)])
        target = Counter(p) 
        left = 0
        res = []

        if window == target:
            res.append(0)
        
        for i in range(len(p),len(s)):
            window[s[i]] += 1
            window[s[left]] -= 1
            left += 1
            
            if window[s[left]] == 0:
                del window[s[left]]

            if window == target:
                res.append(left)
            
        return res
        
