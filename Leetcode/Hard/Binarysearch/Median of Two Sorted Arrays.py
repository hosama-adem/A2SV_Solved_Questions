class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = b = 0
        result = []
        while a < len(nums1) and b < len(nums2):
            n1 = nums1[a]
            n2 = nums2[b]

            if n1 < n2:
                result.append(n1)
                a += 1
            else:
                result.append(n2)
                b +=1
        while a < len(nums1):
            result.append(nums1[a])
            a+=1
        while b < len(nums2):
            result.append(nums2[b])
            b+=1
        
        length =  a + b

        if length % 2 == 0:
            mid = length // 2
            return (result[mid] + result[mid-1])/2
        else:
            return result[length//2]
