class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        import collections
        files=defaultdict()
        result=[]

        for file in paths:
            value= file.split()
        
            for i in  range(1,len(value)):
                val,key = value[i].split("(")
                if key in files:
                    val = value[0]+"/" + val

                    files[key].append(val)
                else:
                    val = value[0] +"/"+ val
                    files[key] = [val]
        for i in files:
            if len(files[i])>=2:
                result.append(files[i])

        return result
