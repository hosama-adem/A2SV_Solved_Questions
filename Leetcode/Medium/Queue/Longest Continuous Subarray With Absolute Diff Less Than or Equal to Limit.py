class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q= deque()#decreasing
        min_q = deque() #increasing
        left = 0
        res = 0

        for i in range(len(nums)):
            while min_q and min_q[-1] > nums[i]:
                min_q.pop()
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            max_q.append(nums[i])
            min_q.append(nums[i])

            while max_q[0]-min_q[0] > limit:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1

            res = max(res,i-left+1)

        return res


            # while len(queue)>=2 and abs(min(queue)-max(queue))<= limit:
                # count += 1
            
            

        
