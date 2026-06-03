class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def step_1(l):
            step = 0
            if l == 1:
                return step
            elif l%2:
                step += 1
                step_1(l*3+1)
            else:
                step += 1
                step_1(l/2)
        
        powe = []
        for i in range(lo, hi+1):
            h = step_1(i)
            powe.append(h)
        
        return powe[k-1]
            
