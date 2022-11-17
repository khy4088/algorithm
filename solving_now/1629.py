import sys

A, B, C = map(int, sys.stdin.readline().split())


for i in range(B):
    A *= A
    if A > C:
        A %= C

print(A%C)