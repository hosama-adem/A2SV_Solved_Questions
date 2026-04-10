#hos
def solve():
    n, k = map(int,input().split())
    a = input()

    count = 0
    for i in range(k):
        if a[i] == "W":
            count += 1
        
    ans = count
    for i in range(k,n):
        if a[i - k] == "W":
            count -= 1
        
        if a[i] == "W":
            count += 1
        
        ans = min(ans, count)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
