#hos
s = input()
count  = 0
stack = [-1]
max_l = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i) #append it the current index if it is (
    else:
        stack.pop()
        if not stack: #if stack is empty append the current index
            stack.append(i)
        curr = i - stack[-1]
        if curr > max_l:
            max_l = curr
            count = 1
        elif curr == max_l:
            count += 1
    
if max_l == 0:
    print(0,1)
else:
    print(max_l, count)
   
