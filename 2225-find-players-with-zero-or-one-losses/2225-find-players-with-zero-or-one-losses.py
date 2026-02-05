class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner={}
        loser={}

        for win , lose in matches:
            winner[win] = winner.get(win,0)+1
            loser[lose] = loser.get(lose,0)+1
        print(winner,loser)
        winu = []
        losu = []
        

        for j in loser:
            if loser [j] == 1:
                losu.append(j)

        for i in winner:
            if winner[i]>=1 and i not in loser:
                winu.append(i)
        losu.sort()
        winu.sort()
           
        return ([winu,losu])
            
        
        