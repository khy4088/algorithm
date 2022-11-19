import sys

A, B, C = map(int, sys.stdin.readline().split())


result = 1

while B > 0:
    if B % 2:
        result *= A
    A *= A
    B //= 2
    A %= C

print(result % C)