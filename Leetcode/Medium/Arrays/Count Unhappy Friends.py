class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0]*n for _ in range(n)]
        for i, pref in enumerate(preferences):
            for j,p in enumerate(pref):
                rank[i][p] = j


        partner = {}

        for x,y in pairs:
            partner[x], partner[y] = y, x

        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break
                if rank[u][x] < rank[u][partner[u]]:
                    unhappy += 1
                    break

        return unhappy        
