class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        #check the if it is inbound
        def inBound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(grid, visited, row, col):
            visited[row][col] = True
            permiter = 0
            
            #for each direction of grid check the perimeter
            for row_c, col_c in directions:
                new_r = row + row_c
                new_c = col + col_c

                if not inBound(new_r, new_c) or grid[new_r][new_c] == 0:
                    permiter += 1
                elif not visited[new_r][new_c]:
                    permiter += dfs(grid, visited, new_r, new_c)
               
            return permiter
        
        #caluclate the dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, visited, i, j)
        

