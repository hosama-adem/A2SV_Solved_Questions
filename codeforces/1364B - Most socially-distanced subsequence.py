#hos

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    if n == 2:
        print(2)
        print(a[0],a[1])
        continue
    
    sub = [a[0]]
    for i in range(1,n-1):
        if (a[i] < a[i-1] and a[i] < a[i+1]) or (a[i] > a[i-1] and a[i] > a[i+1]):
            sub.append(a[i])
    
    sub.append(a[-1])

    print(len(sub))
    print(*sub)
