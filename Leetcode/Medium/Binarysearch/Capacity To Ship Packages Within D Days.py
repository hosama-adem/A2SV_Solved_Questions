class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity,weights):
            day = 1
            current = 0
            for weight in weights:
                if weight + current > capacity:
                    day += 1
                    current = weight

                else:
                    current += weight
            return day <= days

        ans = -1
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (right + left )//2
            if check(mid,weights):
                ans = mid
                right = mid - 1

            else:
                left = mid + 1
            
        return ans
