#hos 
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    ca = []
    for i in range(n):
        l,r,real = map(int,input().split())
        ca.append((l,r,real))
    ca.sort()
    ans = x
    found = True

    while found:
        found = False
        for i in range(len(ca)):
            l,r,real = ca[i]
            if l <= ans <= r:
                if real > ans:
                    ans = real
                    found = True
                ca[i] = (-1,-1,-1)
        
    print(ans)
