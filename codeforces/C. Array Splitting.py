#hos
t,k = map(int,input().split())
a = list(map(int,input().split()))
l = []
for i in range(1,t):
    l.append(a[i]-a[i-1])

l.sort(reverse = True)
d = 0
for i in range(k-1):
    d += l[i]

print(sum(l) - d)
