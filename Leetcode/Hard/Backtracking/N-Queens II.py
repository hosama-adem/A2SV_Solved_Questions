class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        neg_d = set()
        pos_d = set()
        res = 0

        table = [["."]*n for i in range(n)]
        def backtrack(row):
            nonlocal res 
            if row == n:
                all = ["".join(r) for r in table]
                res += 1
                return
            
            for c in range(n):
                if c in col or (row + c) in pos_d or (row-c) in neg_d :
                    continue

                col.add(c)
                pos_d.add(row + c)
                neg_d.add(row - c)
                table[row][c] = "Q"

                backtrack(row + 1)

                col.remove(c)
                pos_d.remove(row + c)
                neg_d.remove(row - c)
                table[row][c] = "."
            
        backtrack(0)
        return res
               
            
