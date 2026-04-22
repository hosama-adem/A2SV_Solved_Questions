class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        dict = Counter(s1) + Counter(s2)
        
        strings = []

        for value in dict.values():
            if value%2 :
                return -1

        swaps = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                strings.append(s1[i]+s2[i])
        
        xy_count = strings.count("xy")
        yx_count = strings.count("yx")
        
        if xy_count%2 == 0 and yx_count%2 == 0:
            swaps+=((xy_count//2)+(yx_count//2))
        else:
            mod = (xy_count//2)+(yx_count//2)
            mod += 2
            swaps += mod

        return swaps
        

                

        

        
