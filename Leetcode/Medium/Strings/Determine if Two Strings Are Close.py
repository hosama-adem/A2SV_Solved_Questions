class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if set(word1) != set(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)
        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())

        if freq1 == freq2:
            return True

        return False

        
        
