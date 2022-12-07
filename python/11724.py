import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().rstrip().split())

E = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

def dfs(visit):
    visited[visit] = True
    for i in E[visit]:
        if not visited[i]:
            dfs(i)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    E[u].append(v)
    E[v].append(u)
    
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)