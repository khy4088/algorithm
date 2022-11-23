import sys

N = int(input())

a = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    
    if x not in a:
        a[x] = []
    a[x].append(y)
    
for i in sorted(a.keys()):
    for t in sorted(a[i]):
        print(' '.join([str(i), str(t)]))