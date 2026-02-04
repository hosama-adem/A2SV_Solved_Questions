def swap_case(s):
    d=""
    for i in s:
        if i==i.upper():
            d+=i.lower()
        else:
            d+=i.upper()
    return d
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
