class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_s = sorted(s , key = lambda x : (-freq[x],x))
        result = "".join(sorted_s)
        return result


        
