import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

NxN = [[0] * (N + 1) for _ in range(N + 1)]
D = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    temp = [0]
    temp_input = list(map(int, sys.stdin.readline().rstrip().split()))
    temp.extend(temp_input)
    NxN[i] = temp


for i in range(1, N + 1):
    for j in range(1, N + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] + NxN[i][j] - D[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    print(D[x2][y2] + D[x1-1][y1-1] - D[x1-1][y2] - D[x2][y1-1])