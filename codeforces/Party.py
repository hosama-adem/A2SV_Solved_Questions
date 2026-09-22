#hos
n = int(input())

a = []

for i in range(n):
    t = int(input())
    a.append(t)

ans = 0

for i in range(n):
    x = i
    count = 1

    while a[x] != -1:
        count += 1
        x = a[x]-1

    ans = max(ans, count)

print(ans)
