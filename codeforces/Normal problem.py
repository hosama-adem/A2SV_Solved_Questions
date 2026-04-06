#hos
t = int(input())
for _ in range(t):
    a = input()
    a = a[::-1]
    nor = ""
    for i in range(len(a)):
        if a[i] == "q":
            nor += "p"
        elif a[i] == "p":
            nor += "q"
        else:
            nor += a[i]
    
    print(nor)
        

