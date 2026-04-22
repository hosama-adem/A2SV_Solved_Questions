class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range (len(nums)):
            nums[i] = str(nums[i])

        def compare(a,b):
            if a+b > b+a:
                return -1
            elif b+a < b+a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))
        result = "".join(nums)

        if result[0] == "0":
            return result[0]
        
        return result
        

        
