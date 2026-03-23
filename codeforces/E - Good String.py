n = int(input())
s = input()
a = []

for i in s:
    if len(a) % 2 :
        if a[-1] ==  i:
            a.pop()
        a.append(i)
    
    else:
        a.append(i)

if len(a) % 2:
    a.pop()

print(n - len(a))
print("".join(a))
