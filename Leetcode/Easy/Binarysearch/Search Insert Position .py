class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 1
        right = len(nums) - 1
        bad = -1

        while left <= right:
            mid = (left + right )//2
            if nums[mid] == target:
                bad = mid
                break
            elif nums[mid] < target:
                bad = mid + 1
                left = mid + 1
            else:
                bad = mid - 1
                right = mid -1
        
        return bad

        
