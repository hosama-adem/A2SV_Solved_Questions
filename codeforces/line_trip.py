t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max1  = a[0]

    for i in range(1,n):
        new = a[i] - a[i-1]
        max1 = max(max1, new)

    r = 2*(x - a[-1])
    val = max(max1, r)
    print(val)
