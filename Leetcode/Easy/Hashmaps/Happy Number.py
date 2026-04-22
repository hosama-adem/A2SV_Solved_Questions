class Solution:
    def isHappy(self, n: int) -> bool:

        def sumofSquares(t):
            s = str(t)
            sum1 = 0
            for i in s:
                sum1 += (int(i)**2)
            return sum1

        multiples = set()
        while n not in multiples:
            multiples.add(n)
            n= sumofSquares(n)
            if n== 1:
                return True
        
        return False

        
        
