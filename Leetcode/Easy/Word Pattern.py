class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = defaultdict()
        s = s.split(" ")

        if len(set(s)) != len(set(pattern)):
            return False

        if len(s)!=len(pattern):
            return False
            
        for i in range(len(s)):
            if pattern[i] in dict and dict[pattern[i]] != s[i]:
                return False
            elif pattern[i] not in dict :
                dict[pattern[i]] = s[i]
            
        return True
