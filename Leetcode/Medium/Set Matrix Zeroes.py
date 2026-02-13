class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = set()
       
        for rows in range(len(matrix)):
            found = False
            for col in range(len(matrix[0])):
                if matrix[rows][col] == 0:
                    found = True
                    column.add(col)
                    
            if found :
                matrix[rows] = [0]*len(matrix[0])
    
        for rowu in range(len(matrix)):
            for colu in range(len(matrix[0])):
                if colu in column :
                    matrix[rowu][colu] = 0
                    

