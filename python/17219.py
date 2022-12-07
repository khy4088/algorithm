import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

result = {}

for _ in range(N):
    site, password = map(str, sys.stdin.readline().rstrip().split())
    result[site] = password
    
for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(result[site])