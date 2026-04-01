class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr , k):
            arr[:k] = arr[:k][::-1]

        result = []

        for i in range(len(arr),1,-1):
            if arr[i-1] != i:
                idx = arr.index(i)
                flip(arr, idx + 1)
                result.append(idx + 1)
                flip(arr , i)
                result.append(i)
        
        return result
            
        


        
