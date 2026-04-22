class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg_d = set()
        pos_d = set()
        res = []

        table = [["."]*n for i in range(n)]
        def backtrack(row):
            if row == n:
                all = ["".join(r) for r in table]
                print(all)
                res.append(all)
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
               
            
