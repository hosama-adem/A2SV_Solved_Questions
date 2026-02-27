#hos
from collections import Counter 
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_count = Counter(a)
b_count = Counter(b)
equal = 0

for i in a_count:
    if i in b_count:
        equal += (a_count[i]*b_count[i])

print(equal)

