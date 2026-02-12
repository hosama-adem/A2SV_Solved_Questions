class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        for i  in range(len(responses)):
            unique = list(set(responses[i]))
            responses[i] = unique

        #counting freq for all words
        freq = {}
        for words in responses:
            for word in words:
                freq[word] = freq.get(word,0)+1

        #get all have maximum freq words
        maximum = max(freq.values())
        res = set()
        for key,val in freq.items():
            if val == maximum:
                res.add(key)

        res = list(res)
        res.sort()
        return res[0]
        
