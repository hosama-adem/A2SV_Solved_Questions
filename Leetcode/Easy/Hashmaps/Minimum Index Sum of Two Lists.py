class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least={}
        res=[]

        for i in range(len(list1)):
            for j in range (len(list2)):
                if list1[i] == list2[j]:
                    least[list1[i]] = i+j
        
        minu=min(least,key=least.get)
     
        for i,val in least.items():
            if val == least[minu]:
                res.append(i)
        
        return res
        
