n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for i in range(len(matrix)):
    for j in range (len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
print()
for i in range(len(matrix[i])):
    for j in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print()