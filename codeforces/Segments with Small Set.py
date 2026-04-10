#hos
def solve():
    from collections import defaultdict
    n, k = map(int,input().split())
    a = list(map(int,input().split()))


    freq = defaultdict(int)
    dist  = left = ans = 0

    for right in range(n):
        if freq[a[right]] == 0:
            dist += 1
        freq[a[right]] += 1
        while dist > k:
            freq[a[left]] -= 1 
            if freq[a[left]] == 0:
                dist -= 1
            
            left += 1

        
        ans += (right - left + 1)

    print(ans)

solve()
