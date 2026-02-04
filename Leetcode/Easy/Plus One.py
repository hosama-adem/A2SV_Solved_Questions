class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs=""

        for i in digits:
            strs+=str(i)
        strs=int(strs)
        strs+=1
        strs=str(strs)
        res=[]
        for i in strs:
            res.append(int(i))
        return(res)
