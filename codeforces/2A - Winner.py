#hos
def solve():
    t = int(input())
    maxu = ""
    ma = 0
    dict1 = {}

    arr = []

    for i in range(t):
        a, b = input().split(" ")
        b = int(b)
        arr.append((a, b))

        if a not in dict1:
            dict1[a] = b
        else:
            dict1[a] += b

    ma = max(dict1.values())

    dict2 = {}

    for a, b in arr:
        dict2[a] = dict2.get(a, 0) + b

        if dict2[a] >= ma and dict1[a] == ma:
            print(a)
            return


solve()
