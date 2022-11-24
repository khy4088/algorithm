import sys
N, K = map(int, sys.stdin.readline().rstrip().split())


result = 1

for i in range(2, N+1):
    result = (result + K - 1) % i + 1

print(result)