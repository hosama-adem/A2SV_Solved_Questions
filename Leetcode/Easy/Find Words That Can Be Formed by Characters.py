class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        len_gs=0
    
        for word in words:
            found = True
        
            for i in set(word):
                if chars.count(i) < word.count(i):
                    found=False
                    break
                
            if found  :
                len_gs += len(word)
        
            
        return len_gs


        
