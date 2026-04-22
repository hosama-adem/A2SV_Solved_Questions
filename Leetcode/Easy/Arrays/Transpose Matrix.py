class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        i = 0
        while i < len(matrix[0]):
            new_col = []
            for row in range(len(matrix)):
                new_col.append(matrix[row][i])
                
            res.append(new_col) 
            i += 1
        
        return res
