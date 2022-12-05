import sys

N = int(input())

for _ in range(N):
    wear = {}
    M = int(input())
    for _ in range(M):
        cloth, cloth_type = map(str, sys.stdin.readline().rstrip().split())
        if cloth_type in wear:
            wear[cloth_type].append(cloth)
        else:
            wear[cloth_type] = ['', cloth]
    t = 1
    for i in wear:
        t *= len(wear[i])
    print(t - 1)