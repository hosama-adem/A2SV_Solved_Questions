class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        tot = 0 

        for i,val in count.items():
            group_size = i+1
            groups = ceil(val / group_size)
            tot += group_size*groups
        
        return tot
