#hos
def solve():
    n = int(input())
    children = [[] for _ in range(n + 1)]

    #constructing the tree
    for i in range(2, n + 1):
        p = int(input())
        children[p].append(i)

    #check the non-leaf node are valid (have at least 3 child )
    for i in range(1, n + 1):
        if len(children[i]) == 0:
            continue
        
        leaf_n = 0
        for child in children[i]:
            if len(children[child]) == 0:
                leaf_n += 1
            
        if leaf_n  < 3:
            print("No")
            return
    
    print("Yes")

solve()
