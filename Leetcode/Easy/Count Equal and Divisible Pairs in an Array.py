class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        the_set=set(nums)
        if len(the_set)==len(nums):
            return(0)
        else:
            count1=0
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j and nums[i]==nums[j] and ((i*j)%k==0):
                        count1+=1
            return count1//2

                       
