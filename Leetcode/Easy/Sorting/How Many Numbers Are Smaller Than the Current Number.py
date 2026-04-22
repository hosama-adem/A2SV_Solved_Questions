class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_nums = sorted(nums)
        print(sorted_nums)

        for i in nums:
            for j,num in enumerate (sorted_nums):
                if i == num  :
                    ans.append(j)
                    break
        


        
        return ans
