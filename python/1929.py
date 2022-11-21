import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

che = [True] * (N + 1)

che[1] = False

for i in range(2, N + 1):
    if che[i] == True:
        for j in range(i + i, N + 1, i):
            che[j] = False


for i in range(M, N + 1):
    if che[i] == True:
        print(i)