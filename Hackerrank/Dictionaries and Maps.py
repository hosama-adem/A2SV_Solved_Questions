# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
freq = {}

for _ in range(n):
    name,p_num=input().split()
    freq[name] = p_num
    
for line in sys.stdin:
    query = line.strip()
    if query in freq:
        print(f"{query}={freq[query]}")
    else:
        print("Not found")
    
