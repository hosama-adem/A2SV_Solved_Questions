class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        middle = float("-inf")

        for num in reversed (nums):
            if num < middle:
                return True
            while stack and num > stack[-1]:
                middle = stack.pop()
            
            stack.append(num)
        
        return False
