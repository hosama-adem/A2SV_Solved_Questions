t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = [0] * (n + 2)
    s[a[0]] = 1
    ok = 1

    for x in a[1:]:
        if not (s[x - 1] or s[x + 1]):
            ok = 0
            break
        s[x] = 1

    print("YES" if ok else "NO")
