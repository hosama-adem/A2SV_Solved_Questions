class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_of_evens = sum(i for i in nums if i%2 == 0)

        for num , ind in queries:
            if nums[ind] % 2:
                nums[ind] = nums[ind]+num
                if nums[ind]%2 == 0:
                    sum_of_evens += nums[ind]
                    res.append(sum_of_evens)
                else:
                    res.append(sum_of_evens)
            else:
                sum_of_evens -= nums[ind]
                nums[ind] = nums[ind]+num
                if nums[ind]%2 == 0:
                    sum_of_evens += nums[ind]
                    res.append(sum_of_evens)
                else:
                    res.append(sum_of_evens)
                
        return res

        
