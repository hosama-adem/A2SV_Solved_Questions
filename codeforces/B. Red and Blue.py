#hos
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    cur = 0
    maxu1 = 0
    for i in range(n):
        cur += a[i]
        maxu1 = max(maxu1, cur)
    
    cur  = 0
    maxu2 = 0
    for i in range(m):
        cur += b[i]
        maxu2 = max(maxu2, cur)
    
    print(maxu1 + maxu2)
