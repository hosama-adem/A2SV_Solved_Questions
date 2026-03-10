class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == "../" and not stack :
                continue
            elif log == "../":
                stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
            
        return len(stack)

        
