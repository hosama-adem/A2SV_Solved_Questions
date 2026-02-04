class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #finally i got it
        result=[]
        found=True
        su=""

        for  i in source:
            
            j=0
            while j <len(i):
                if found and j+1<len(i) and i[j]=="/" and i[j+1]=="*":
                    found=False
                    j+=2

                elif  found and j+1<len(i) and i[j]=="/" and i[j+1]=="/":    
                        break

                elif not found and j+1<len(i) and i[j]=="*" and i[j+1]=="/":
                        j+=2
                        found=True

                elif found:
                        su+=i[j]
                        j+=1
                else:
                    j+=1

                    
            if found and su:
                result.append(su)
                su=""

        return result


                
         
