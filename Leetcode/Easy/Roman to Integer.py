class Solution:
    def romanToInt(self, s: str) -> int:
        pair = {"I":1 , "V":5 ,"X":10 , 
                    "L":50,"C":100 , "D":500 ,"M":1000}
        
        value = 0
        i = 0
        while i < len(s)-1:
            if pair[s[i]] < pair [s[i+1]]:
                value -= pair[s[i]]
                value += pair [s[i+1]]
                i+=2
            else:
                value += pair[s[i]]
                i+=1
                
        if i == len(s)-1:
            value += pair[s[i]]
      
        return value
        



        
