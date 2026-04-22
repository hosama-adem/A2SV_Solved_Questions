class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        result = []

        for i in range(n + m -1):
            diag = []

            for j in range(n):
                k = i - j
                if 0 <= k < m:
                    diag.append(mat[j][k])
                
            if i % 2 == 0:
                diag.reverse()
            
            result.extend(diag)
        

        
        return result 

        
