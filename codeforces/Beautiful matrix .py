#hos
matrix = []
for i in range(5):
    a = list(map(int,input().split()))
    matrix.append(a)

row , column = 0 , 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row ,column =i,j

ans = abs(row-2) + abs(column-2)
print(ans)
