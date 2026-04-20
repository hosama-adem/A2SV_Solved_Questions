#hos
def solve():
    t = int(input())
    dict1 = {}
    set1 = set()

    for _ in range(t):
        a = input()
        
        if a not in set1:
            set1.add(a)
            dict1[a] = 1
            print("OK")
        else:
            s =str(dict1[a])
            print(a+s)
            dict1[a] += 1
    
solve()
        
