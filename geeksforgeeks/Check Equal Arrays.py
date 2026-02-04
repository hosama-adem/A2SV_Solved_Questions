class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a_sorted = sorted(a)
        b_sorted = sorted(b)
        
        if a_sorted == b_sorted:
            return True
        else:
            return False
