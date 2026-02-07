class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict=Counter(nums)
        all={i for i in dict if dict[i]>len(nums)/3} 
        return(list(all))
