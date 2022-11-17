import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
result = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if numbers[i] == numbers[-1-j]:
            result[i][N-j-1] = 1
        else:
            result[i][N-j-1] = 0

M = int(sys.stdin.readline())
answer = []
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    status = True
    for i in range((E-S+1) // 2 + 1):
        # print(result[i][E-1-i])
        if result[i][E-1-i] == 0:
            answer.append(0)
            status = False
            break
    if status:
        answer.append(1)

for a in answer:
    print(a)
