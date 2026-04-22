class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":'jkl',
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"
                }

        com = []
        def backtrack(ind,curr):
            if len(curr) == len(digits):
                com.append(curr)
                return 
            
            for i in comb[digits[ind]]:
                backtrack(ind + 1 ,curr + i)
        
        if digits:
            backtrack(0,"")
        return com
            
            
