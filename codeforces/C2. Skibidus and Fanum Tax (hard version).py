#hos
import bisect 
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    prev = -float("inf")
    b.sort()
    
    for i in range(n):
        best = float("inf")
        if a[i] >= prev:
            best = min(a[i],best)

        tar = a[i] + prev
        idx = bisect.bisect_left(b,tar) 

        if idx < m:
            val = b[idx] - a[i]
            best = min(best,val)

        if best == float("inf"):
            print("NO")     
            break
    
        prev = best
    
    else:
        print("YES")
