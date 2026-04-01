n,x = map(int,input().split())
a = list(map(int,input().split()))

res = l = 0
curr = 0

for i in range(n):
    curr += a[i]
    while curr > x -1:
        curr -= a[l]
        l += 1
    
    res += i - l + 1

# get small sum and we can use total minus small sum
tot = n * (n + 1) // 2

print(tot - res)
