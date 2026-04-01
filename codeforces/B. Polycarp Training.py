#hos
t = int(input())
a = list(map(int,input().split()))

a.sort()
days = 0
for i in range(t):
    if  a[i] > days:
        days += 1
    

print(days)
