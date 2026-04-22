#hos
from collections import defaultdict
t = int(input())
dict1 = defaultdict(int)
for _ in range(t):
    a = input()
    dict1[a] = dict1.get(a, 0) + 1

maxu = max(dict1,key = dict1.get)
print(maxu)
