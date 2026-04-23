class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def inBound(row, col):
            return (0 <= row < rows and  0 <= col < cols)
        
        def dfs(row, col):
            grid[row][col] == "0"
            
            for row_c, col_c in directions:
                new_r, new_c = row_c + row, col_c + col
                if inBound(new_r, new_c) and grid[new_r][new_c] == "1":
                    return dfs(new_r, new_c)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands
