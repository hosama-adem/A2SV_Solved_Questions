#hos
def solve():
    from collections import defaultdict
    t = int(input())
    for _ in range(t):
        n = int(int(input()))
        a = list(map(int,input().split()))
        
        count = 0
        freq = defaultdict(int)
        for i in range(n):
            key = i - a[i]
            count += freq[key]
            freq[key] += 1
        
        # print(freq)
        print(count)


solve()
