class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)

        for ch in count1:
            if count2[ch]<count1[ch]:
                return False
        
        return True


        
