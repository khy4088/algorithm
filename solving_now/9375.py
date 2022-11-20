import sys
from itertools import product

N = int(input())

case = []

for _ in range(N):
    wear = {}
    M = int(input())
    for _ in range(M):
        cloth, cloth_type = map(str, sys.stdin.readline().rstrip().split())
        if cloth_type in wear:
            wear[cloth_type].append(cloth)
        else:
            wear[cloth_type] = [cloth]
    wears = tuple(wear.values())
    print(len(list(product(*wears))))