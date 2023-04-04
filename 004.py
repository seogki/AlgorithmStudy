# 2차원 배열 합
# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

# 22,34 / 34,34 / 11,44

n, m = map(int, input().split())

A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

print(A)

for i in range(1, n +1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
#       D[1][1] = D[1][0] + D[0][1] - D[0][0] + A[1][1]
#       1 = 0 + 0 - 0 + 1
print(D)

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1 -1][y1 - 1]
    print(result)