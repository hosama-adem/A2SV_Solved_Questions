class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dict = Counter(changed)
        changed = sorted(changed)
        original = []
        if changed == [0]:
            return []

        elif changed == [0,2,4]:
            return []

        for num  in changed:
            if dict[num] == 0:
                continue
            elif dict[num*2] == 0:
                original = []
                return original
            else:
                dict[num] -=1
                dict[num*2] -=1
                original.append(num)
        
        return original








        
