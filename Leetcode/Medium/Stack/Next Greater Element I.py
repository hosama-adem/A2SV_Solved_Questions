class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            inde = nums2.index(num)
            next_g = -1
            for i in range(inde+1,len(nums2)):
                if nums2[i] > num:
                    next_g = nums2[i]
                    break
            
            ans.append(next_g)
        
        return ans


            
        
