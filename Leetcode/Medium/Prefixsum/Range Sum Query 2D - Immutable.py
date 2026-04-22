class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Rows,Cols = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(Cols + 1) for i in range(Rows + 1)]

        for i in range(Rows):
            pre = 0
            for j in range(Cols):
                pre += matrix[i][j]
                above = self.sumMat[i][j + 1]
                self.sumMat[i + 1][j + 1] = pre + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom =self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topleft = self.sumMat[row1 -1][col1 - 1]
        return bottom - left - above + topleft 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
