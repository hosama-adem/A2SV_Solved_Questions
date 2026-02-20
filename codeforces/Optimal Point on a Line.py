#hos
t = int(input())
a = list(map(int,input().split()))
a.sort()

short = len(a)//2

if len(a) % 2 == 0:
    print(a[short-1])
else:
    print(a[short])
