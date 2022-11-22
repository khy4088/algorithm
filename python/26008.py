import sys


N, M, A = map(int, sys.stdin.readline().rstrip().split())

H = int(input())


print(pow(M, N-1, 1000000007))