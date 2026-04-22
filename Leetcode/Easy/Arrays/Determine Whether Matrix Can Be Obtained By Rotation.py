class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotation_90(mat):
            for i in range(len(mat)):
                for j in range(i+1,len(mat)):
                    mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
                
            for i in range(len(mat)):
                mat[i].reverse()
        
        for i in range(4):
            if mat == target:
                return True 
            rotation_90(mat)
            
        return False
        
