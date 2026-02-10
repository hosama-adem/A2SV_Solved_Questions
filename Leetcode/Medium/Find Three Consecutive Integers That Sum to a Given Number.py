class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        div = num//3
        if div +(div+1)+(div-1) == num:
            return[div-1,div,div+1]
        if div + (div+1) + (div+2) == num:
            return [div ,div+1, div+2 ]
        
        return []   
        
        
