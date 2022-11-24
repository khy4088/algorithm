import sys

N = int(input())

a = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    
    if y not in a:
        a[y] = []
    a[y].append(x)
    
for i in sorted(a.keys()):
    for t in sorted(a[i]):
        print(' '.join([str(t), str(i)]))