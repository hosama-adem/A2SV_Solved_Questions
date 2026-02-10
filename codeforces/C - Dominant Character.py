t = int(input())
for _ in range(t):
    n = int(input())
    a = input()

    if "aa" in a:
        print(2)
        
    elif "aca" in a or "aba" in a :
        print(3)
    elif "acba" in a or "abca" in a :
        print(4)
    elif "accabba" in a or "abbacca" in a:
        print(7)
    else:
        print(-1)
    
