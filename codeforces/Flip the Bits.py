#hos
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    bal = 0
    good = [False] * n
    for i in range(n):
        if a[i] == "1":
            bal += 1
        else:
            bal -= 1
        
        if bal == 0:
            good[i] = True
        
    
    flip = 0
    poss = True

    for i in range(n-1, -1, -1):
        curr = a[i]

        if flip:
            curr = "1" if curr == '0' else '0'
        if curr != b[i]:
            if not good[i]:
                poss = False
                break
            
            flip ^= 1
        

    print("YES" if poss else "NO")
        
    
