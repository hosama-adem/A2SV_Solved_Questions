class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row , col = len(img), len(img[0])
        res = [[0]*col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                tot,cnt  = 0, 0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if i == row or j == col or i < 0 or j < 0:
                            continue
                        tot += img[i][j] 
                        cnt += 1

                res[r][c] = tot//cnt
            
        return res
