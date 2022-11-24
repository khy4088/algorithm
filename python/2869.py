import sys
from math import ceil

A, B, V = map(int, sys.stdin.readline().split())

day = (V - B) / (A - B)
print(ceil(day))