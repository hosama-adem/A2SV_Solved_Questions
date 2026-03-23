from collections import defaultdict, deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

length = defaultdict(list)

min_q = deque()
max_q = deque()

left = 0

for right in range(n):
    
    while min_q and a[min_q[-1]] > a[right]:
        min_q.pop()
    min_q.append(right)

    while max_q and a[max_q[-1]] < a[right]:
        max_q.pop()
    max_q.append(right)

    # shrink window
    while a[max_q[0]] - a[min_q[0]] > k:
        if min_q[0] == left:
            min_q.popleft()
        if max_q[0] == left:
            max_q.popleft()
        left += 1

    cur_len = right - left + 1
    length[cur_len].append((left + 1, right + 1))

maxu = max(length)
count = len(length[maxu])

print(maxu, count)
for start, end in length[maxu]:
    print(start, end)
