if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr=set(arr)
    new_arr2=sorted(new_arr)
    print(new_arr2[-2])
