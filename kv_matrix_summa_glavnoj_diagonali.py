n = int(input())
matrix = [input().split() * n for _ in range(n)]
total = 0
for i in range(n):
    total += int(matrix[i][i])
print(total)
