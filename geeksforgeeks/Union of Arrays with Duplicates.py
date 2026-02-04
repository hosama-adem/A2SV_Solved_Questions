class Solution:    
    def findUnion(self, a, b):
        # code here
        set_one=set(a+b)
        return(list(set_one))
