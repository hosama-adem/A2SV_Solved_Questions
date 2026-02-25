#hos
t = int(input())
for _ in range(t):
    s = input()
    i = 0
    w = set()

    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        length = j - i
        if length % 2 == 1:
            w.add(s[i])
        
        i = j

    print("".join(sorted(w)))
