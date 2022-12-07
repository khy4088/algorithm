import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline().rstrip())

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

dfs(1)

for i in visited:
    if i == True:
        count += 1
        
print(count - 1)