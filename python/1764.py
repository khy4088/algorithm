import sys

N, M = map(int, sys.stdin.readline().split())

unknown = {}
count = 0
result = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    unknown[temp] = False

for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp in unknown:
        count += 1
        result.append(temp)

print(count)
for r in sorted(result):
    print(r)