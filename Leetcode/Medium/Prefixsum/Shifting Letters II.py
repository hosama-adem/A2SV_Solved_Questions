class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        d = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
             7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 
             14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 
             21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        l=[0]*(len(s)+1)
        for i in shifts:
            if i[2]==0:
                l[i[0]]-=1
                l[i[1] + 1] +=1
            else:
                l[i[0]]+=1
                l[i[1] + 1] -=1
        pref=[l[0]]
        for i in range(1,len(s)):
            pref.append(pref[-1]+l[i])
        chars = [ord(i)-ord('a') for i in s]
        for i in range(len(chars)):
            x =chars[i]+pref[i]
            chars[i] = x%26
        print(chars)
        let = [d[i] for i in chars]
        return ''.join(let)
   
       

