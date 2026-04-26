class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isupper() and stack:
                if stack[-1].islower() and i.lower() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            elif i.islower() and stack:
                if stack[-1].isupper() and i.upper() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
            
        res = "".join(stack)

        return res
