class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = []
        ten = []

        for bill in bills:
            if bill == 5:
                five.append(bill)
            elif bill == 10 and not five:
                return False
            elif bill == 10 and five:
                five.pop()
                ten.append(bill)
            elif bill == 20 and not ten and len(five)<3:
                return False
            elif bill == 20 and not ten:
                five.pop()
                five.pop()
                five.pop()
            elif bill == 20 and five:
                ten.pop()
                five.pop()
            else:
                return False

        return True
        
