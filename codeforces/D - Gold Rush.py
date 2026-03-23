t = int(input())
def check(n,m):
    if n == m:
        return True
    if n < x or n % 3: 
        return False

    return check(n//3,m) or check(2*n//3,m)

for _ in range(t):
    n,x = map(int,input().split())
    # if n < x or n % 3: 

    if check(n,x):
        print("YES")
    else:
        print("NO")


